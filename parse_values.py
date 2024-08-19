import requests
from bs4 import BeautifulSoup

def parse_values(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    all_moves = soup.find_all('tr')

    moves_dict = {}
    for move in all_moves:
        move_name_tag = move.find('span', class_="tooltip")
        if move_name_tag is None:
            continue
        move_name = move_name_tag.text.strip()

        tooltip_text = move.find('span', class_="tooltiptext")
        if tooltip_text is None:
            continue

        move_details = tooltip_text.find_all('span', class_='tmp-item')
        details_dict = {}
        for detail in move_details:
            key = detail.find('span', class_='tmp-item-label').text.strip()
            value = detail.find('span', class_='tmp-item-data').text.strip()
            details_dict[key] = value

        moves_dict[move_name] = details_dict

    return moves_dict

parsed_moves = parse_values("https://www.dustloop.com/w/GBVSR/Gran/Frame_Data")
print(parsed_moves)
