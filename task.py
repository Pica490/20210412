import requests

def compare_heroes(list_heroes):
    intelligens = 0
    for name in list_heroes:
        url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
        response = requests.get(url)
        r = response.json()
        if int(r['results'][0]['powerstats']['intelligence']) > intelligens:
            m_intel = f'Самый умный {name}.'
    return m_intel


if __name__ == '__main__':
    print(compare_heroes(['Hulk', 'Captain America','Thanos']))