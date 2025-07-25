import os

from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient import discovery


CREDENTIALS_FILE = 'second-service-account.json'

# Уровни доступа
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

load_dotenv()

EMAIL_USER = os.environ['EMAIL']

INFO = {
    'type':  os.environ['TYPE'],
    'project_id':  os.environ['PROJECT_ID'],
    'private_key_id':  os.environ['PRIVATE_KEY_ID'],
    "private_key": os.environ["PRIVATE_KEY"].replace("\\n", "\n"),
    'client_email':  os.environ['CLIENT_EMAIL'],
    'client_id':  os.environ['CLIENT_ID'],
    'auth_uri':  os.environ['AUTH_URI'],
    'token_uri':  os.environ['TOKEN_URI'],
    'auth_provider_x509_cert_url':  os.environ['AUTH_PROVIDER_X509_CERT_URL'],
    'client_x509_cert_url':  os.environ['CLIENT_X509_CERT_URL']
}

# CREDENTIALS = Credentials.from_service_account_file(
#     filename=CREDENTIALS_FILE, scopes=SCOPES
# )
CREDENTIALS = Credentials.from_service_account_info(
    info=INFO, scopes=SCOPES)

SHEETS_SERVICE = discovery.build('sheets', 'v4', credentials=CREDENTIALS)
DRIVE_SERVICE = discovery.build('drive', 'v3', credentials=CREDENTIALS)
