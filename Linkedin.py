# Importing Dependencies
import http.client, urllib.request, urllib.parse, urllib.error
import json
import csv
import pandas as pd
from difflib import SequenceMatcher

# Storing file path
file_loc = r'File_location'
xl = pd.ExcelFile(file_loc)
df = xl.parse("Sheet1")
names = df['Name'].tolist()
roles = df['Current Title'].tolist()
companies = df['Current Company'].tolist()

# Secret API key
API_KEY = '670f1c5cc526474787ca05f26600bc81 '

# Creating an array for linkedin
linkedin = []

# zip to loop over names and companies simultaneously
def finder1():
    for name, role, company in zip(names, roles, companies):

        #condition where no role and company are present in data set
        if(role == " " and company == " " or role == "Retired" or role == "Student"):
            linkedin.append([name, role, company, '-'])
            query=''
            check = "check"
            print("no data")
        #condition where only name and role are present in data set
        elif(company == " "):
            query = name + " " + '"' + role +'"' + " " + "site:linkedin.com/in"
            check = name + " " + role
        #name and company
        elif(role == " "):
            query = name + " " + '"' + company + '"' + " " + "site:linkedin.com/in"
            check = name + " " + company
        # name and role
        else:
            query = name + " " + '"' + role + " " + company + '"' + " " + "site:linkedin.com/in"
            check = name + " " + role + " " + company

        print(query)

        try:
            headers = {'Ocp-Apim-Subscription-Key': API_KEY}
            params = urllib.parse.urlencode(
                {'q': query, 'count': '2', 'mkt': 'de-DE'})  # returns top 2 (German) results
            conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
            conn.request("GET", "/bing/v7.0/search?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read().decode('utf-8')
            json_file = json.loads(data)
            conn.close()

            for result in json_file['webPages']['value']:
                title = result['name']
                print(result)
                ratio = SequenceMatcher(None, check.lower(), title.lower()).ratio()
                print(ratio)
                if ratio > 0.5:
                    if r'linkedin.com/in/' in result['displayUrl']:  # checks if the search result URL is a LI profile
                        linkedin.append([name, role, company, result['displayUrl']])
                        break
                else:
                    linkedin.append([name, role, company, '-'])
                    break

        except Exception as e:
            print(e)
            continue

def finder2():
    for name, role, company in zip(names, roles, companies):

        # name and role and company
        if (role == " " and company == " " or role == "Retired" or role == "Student"):
            print("no data")
            query = ' '
            linkedin.append([name, role, company, '-'])
            check = "check"
        # name and role
        elif (company == " "):
            query = '"' + name + ' ' + role + '"' + " " + "site:linkedin.com/in"
            check = name + " " + role
        # name and company
        elif (role == " "):
            query = '"' + name + ' ' + company + '"' + " " + "site:linkedin.com/in"
            check = name + " " + company
            # name and role
        else:
            query = '"' + name + ' ' + role + ' ' + company + '"' + " " + "site:linkedin.com/in"
            check = name + " " + role + " " + company

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
                print(result)
                ratio = SequenceMatcher(None, check.lower(), title.lower()).ratio()
                print(ratio)
                if ratio > 0.5:
                    if r'linkedin.com/in/' in result['displayUrl']:  # checks if the search result URL is a LI profile
                        linkedin.append([name, role, company, result['displayUrl']])
                        break
                else:
                    linkedin.append([name, role, company, '-'])

        except Exception as e:
            print(e)

finder1()
finder2()

# Writing the results to a CSV file
with open('linkedin_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in linkedin:
        writer.writerow(row)

print('Number of LinkedIn profiles found:')
print(len(linkedin))
