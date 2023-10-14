from elasticsearch import Elasticsearch


CERT_FINGERPRINT = "db0ce174fb8c0f00bc1829702963d22ae51604c589238992de269babbeb8e865"

# Password for the 'elastic' user generated by Elasticsearch
ELASTIC_PASSWORD = "AGtLUXVMCQ6G3qhl6Z1b"
try:
    es=Elasticsearch(
        "https://localhost:9200",
        ssl_assert_fingerprint=CERT_FINGERPRINT,
        basic_auth=("elastic", ELASTIC_PASSWORD)
    )
except ConnectionError as e:
    print("Connection Error:", e)
    
if es.ping():
    print("Succesfully connected to ElasticSearch!!")
else:
    print("Oops!! Can not connect to Elasticsearch!")



import pandas as pd

df = pd.read_csv("myntra_products_catalog.csv").loc[:499]
df.head()

df.fillna("None", inplace=True)

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-mpnet-base-v2')

df["DescriptionVector"] = df["Description"].apply(lambda x: model.encode(x))

from indexMapping import indexMapping

es.indices.create(index="all_products", mappings=indexMapping)


record_list = df.to_dict("records")

for record in record_list:
    try:
        es.index(index="all_products", document=record, id=record["ProductID"])
    except Exception as e:
        print(e)


es.count(index="all_products")

input_keyword = "Blue Shoes"
vector_of_input_keyword = model.encode(input_keyword)

query = {
    "field" : "DescriptionVector",
    "query_vector" : vector_of_input_keyword,
    "k" : 2,
    "num_candidates" : 500, 
}

res = es.knn_search(index="all_products", knn=query , source=["ProductName","Description"])
res["hits"]["hits"]