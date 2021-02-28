
# failes to import json
import requests, bs4, pandas, time, json

# Ask Name and Price
def get_app_info(apple_id):
    url = f'https://apps.apple.com/no/app/id{apple_id}'
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    name_element = soup.find(name='h1', attrs={'class': lambda string: 'title' in string})
    name = str(next(name_element.children)).strip()
    price_element = soup.find(name='li', attrs={'class': lambda string: 'price' in string})
    price = price_element.text.replace('\xa0', ' ')
    time.sleep(0.5)
    return app_id, name, price

#get json file 
with open ("inputFile.json") as file:
    data = json.load(file)

# Make list
lst = list()

#Lopp through objects and put vaules in list
for i in range (len(data["value"])):
    lst.append(data['value'][i]['apple_id'])
    print (lst)

# Main // Get result, (print), export
if __name__ == '__main__':
    results = [get_app_info(apple_id) for app_id in lst]
    df = pandas.DataFrame(results, columns=['apple_id', 'name', 'price'])
    print(df)
    df.to_json('outFile.json')
        
    