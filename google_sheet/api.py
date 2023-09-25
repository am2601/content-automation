import httplib2
from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'credentials.json'
SHEET_ID = '13UNVPGDAxPTPw7GTmH-oTNfiPu-w7E7UwGW3LZ8OdI0'

def read(sheet_id, sheet, range):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',])
    httpAuth = credentials.authorize(httplib2.Http())
    service = discovery.build('sheets', 'v4', http=httpAuth)
    response = service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=f'{sheet}!{range}',
        majorDimension='COLUMNS'
    ).execute()
    print(response.get('values'))

if __name__ == '__main__':
    read(SHEET_ID, 'Sheet1', 'A2:B4')