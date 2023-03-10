from poke_scraper import *
import gspread
import gspread_dataframe, gspread_formatting
from oauth2client.service_account import ServiceAccountCredentials

sheet_name = 'Ultimate Pokedex'

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open(sheet_name)

# For new Pokemon from each generation
for gen_number in range(1, 10):
    url = f"https://www.serebii.net/pokemon/gen{gen_number}pokemon.shtml"
    poke_list = PokeScraper(url)
    df = poke_list.create_gen_df()
    worksheet1 = spreadsheet.add_worksheet(title=f'Gen {gen_number} Checklist', rows='200', cols='15')
    worksheet1.clear()
    gspread_dataframe.set_with_dataframe(worksheet=worksheet1, dataframe=df, include_index=False, include_column_header=True, resize=True)

# For Pokemon regional forms 
regions = {'sunmoon': 'alola', 'swordshield': 'galarian', 'scarletviolet': 'paldean'}
for key, value in regions.items():
    url = f"https://serebii.net/{key}/{value}forms.shtml"
    poke_list = PokeScraper(url)
    df = poke_list.create_region_df()
    worksheet1 = spreadsheet.add_worksheet(title=f'{value.capitalize()} Form Checklist', rows='200', cols='15')
    worksheet1.clear()
    gspread_dataframe.set_with_dataframe(worksheet=worksheet1, dataframe=df, include_index=False, include_column_header=True, resize=True)