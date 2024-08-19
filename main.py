import requests
from bs4 import BeautifulSoup

def get_frame_data(url):

    info = requests.get(url)
    soup = BeautifulSoup(info.text, "html.parser")

    field_names = soup.find_all('span', class_="mw-headline")

    data_name_and_values = {}

    section_values = {}

    table_values = []

    for name in field_names:
        if name.text == "Overview":
            continue
        table = name.find_next('table', {'class': 'cargoTable'})

        if table:
            table_values = table.find_all('tr')

        for table_value in table_values:
            if table_value.find('td') is None:
                continue
            else:
                field_name = table_value.find('td', {'class': 'field_Damage'})
                print(field_name)
                field_value = table_value.find('td')
                print(field_value)

                section_values[field_name] = field_value
        if name.text != "Normal Moves":
            data_name_and_values[name.text] = section_values

    print(data_name_and_values)

get_frame_data("https://www.dustloop.com/w/GBVSR/Gran")

