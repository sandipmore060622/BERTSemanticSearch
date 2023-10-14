# My Project

This is a brief description of my project.

## Installation

To install this project on windows, follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/BERTSemanticSearch.git` on C drive


2. Download `elasticsearch-8.10.3-windows-x86_64.zip` from `https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.10.3-windows-x86_64.zip` and copy it into `BERTSemanticSearch` folder.


2. Open power shell as administrator and Navigate to the project directory: `cd C:\BERTSemanticSearch`


3. Run : `Expand-Archive -Path ".\elasticsearch-8.10.3-windows-x86_64.zip" -DestinationPath ".\elasticsearch-8.10.3"`


4. Run : `cd ".\elasticsearch-8.10.3\elasticsearch-8.10.3"`


5. Run : `.\bin\elasticsearch.bat`


6. Note ELASTIC_PASSWORD and CERT_FINGERPRINT as per following image (observe output from above code run) and replace them in indexData.py and searchApp.py.


![My Image](creds.jpg)

7. Run : `pip install -r requirements.txt`
 

8. Run : `python indexData.py`


9. Run : `python searchApp.py`


10. Run : `streamlit run searchApp.py`



11. Open your web browser and go to `http://localhost:8501/`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
