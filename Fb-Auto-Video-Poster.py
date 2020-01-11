'''
You can get your page acess token by this
https://graph.facebook.com/page_id?fields=access_token&access_token=your_user_token_From_business_manager
Configurations here
'''
import json
import random
import requests 
import urllib
page_id = "" ## My Page id where i want to post
page_access_token = ""
user_access_token = ""
source_page_ids = ['',''] ## Source page ids from where i want to get random photos or memes
source_page_id = random.choice(source_page_ids)
url = "https://graph.facebook.com/"+source_page_id+"/videos?type=uploaded&access_token="+user_access_token
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4'}
response = requests.get(url,headers=user_agent)
json_data = json.loads(response.text)  
total_json_data_length = len(json_data['data'])
random_choice = random.randint(1,total_json_data_length)
json = json_data['data'][random_choice]
try:
	name = json['name']
except:
	name = ""
status_text = name
img_src = json['source']
url = "https://graph.facebook.com/"+page_id+"/videos?file_url="+urllib.quote(img_src)+"&caption="+status_text+"&access_token="+page_access_token
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4'}
response = requests.post(url,headers=user_agent) 
print("Posted Successfully...")

