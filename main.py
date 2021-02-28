
# failes to import json
import requests, bs4, pandas, time, json

# Ask Name and Price
def get_app_info(app_id):
    url = f'https://apps.apple.com/no/app/id{app_id}'
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    name_element = soup.find(name='h1', attrs={'class': lambda string: 'title' in string})
    name = str(next(name_element.children)).strip()
    price_element = soup.find(name='li', attrs={'class': lambda string: 'price' in string})
    price = price_element.text.replace('\xa0', ' ')
    time.sleep(0.5)
    return app_id, name, price

#get json file 
with open ("appArrayInput.json") as file:
    data = json.load(file)

# Make list
lst = list()

#Lopp through objects and put vaules in list
for i in range (len(data["value"])):
    lst.append(data['value'][i]['appId'])
    print (lst)

# Main // Get result, (print), export
if __name__ == '__main__':
    results = [get_app_info(app_id) for app_id in lst]
    df = pandas.DataFrame(results, columns=['app_id', 'name', 'price'])
    print(df)
    df.to_json('appleAppPrices.json')
        
    