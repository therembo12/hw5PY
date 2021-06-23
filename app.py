from modules.module import GetInfo
from modules.module import write_json

response = GetInfo(
    'https://api.privatbank.ua/p24api/exchange_rates?json&date=01.01.2021')
PB = response.get_info()
print(PB)
