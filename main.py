
# Imports
import requests, bs4, pandas, time, json

# Ask Name and Price // FAILS ON GETTING INFO
def get_app_info(apple_id):
    url = f'https://apps.apple.com/no/app/id{apple_id}'
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    name_element = soup.find(name='h1', attrs={'class': lambda string: 'title' in string})
    name = str(next(name_element.children)).strip()
    price_element = soup.find(name='li', attrs={'class': lambda string: 'price' in string})
    price = price_element.text.replace('\xa0', ' ')
    time.sleep(0.5)
    return url #apple_id, name, price

#get json file 
with open ("inputFile.json") as file:
    data = json.load(file)

# Make list
lst = list()

# Isolate apple app ID and append to list // choose url or apple_id // 
for i in range (len(data["value"])):
    splitUrl = (data['value'][i]['informationUrl'].split("/id",1))
    apple_id = (splitUrl[1])
    lst.append(apple_id)
    #lst.append(data['value'][i]['informationUrl'])
print(lst)


# Main // Get result, (print), export
if __name__ == '__main__':
    results = [get_app_info(apple_id) for apple_id in lst]
    df = pandas.DataFrame(results, columns=['apple_id', 'name', 'price'])
    print(df)
    df.to_json('outFile.json')
        
    