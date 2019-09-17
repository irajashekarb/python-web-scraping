# Importing Dependencies
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import csv
import pandas as pd

# Storing file path
file_loc = r'C:\Users\iraja\PycharmProjects\Web Scraping\Scraping websites\project scraping\data_in.xlsx'
xl = pd.ExcelFile(file_loc)
df = xl.parse("Sheet1")
names = df['Name'].tolist()
roles = df['Current Title'].tolist()
companies = df['Current Company'].tolist()

# Secret API key
API_KEY = '339e8339f5cc478fabc12cefdf2e738e'

linkedin = []

# zip to loop over names and companies simultaneously
for name, role, company in zip(names, roles, companies):

    query = name + " " + role + " " + company
    print(query)
    try:
        headers = {'Ocp-Apim-Subscription-Key': API_KEY}
        params = urllib.parse.urlencode({'q': query, 'count': '2', 'mkt': 'de-DE'})  # returns top 2 (German) results
        conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v7.0/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        json_file = json.loads(data)
        conn.close()

        for result in json_file['webPages']['value']:
            title = result['name']
            if name.lower() in title.lower():  # checks if the name appears in the title
                if 'linkedin.com/in/' in result['displayUrl']:  # checks if the search result URL is a LI profile
                    linkedin.append([name, role, company, result['displayUrl']])
                    break

    except Exception as e:
        print(e)
        continue

# Writing the results to a CSV file
with open('linkedin_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in linkedin:
        writer.writerow(row)

print('Number of LinkedIn profiles found:')
print(len(linkedin))