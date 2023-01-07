from poke_scraper import df
import gspread
import gspread_dataframe, gspread_formatting
from oauth2client.service_account import ServiceAccountCredentials

sheet_name = 'Ultimate Pokedex'

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open(sheet_name)
worksheet1 = spreadsheet.add_worksheet(title='Gen 3 Checklist', rows='200', cols='15')
worksheet1.clear()
gspread_dataframe.set_with_dataframe(worksheet=worksheet1, dataframe=df, include_index=False, include_column_header=True, resize=True)