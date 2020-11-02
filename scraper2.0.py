import requests
import json
from bs4 import BeautifulSoup

def main():
	pages_list=[]
	for i in range(1,82200):
			URL = f'https://dawahnigeria.com/dawahcast/a/{i}'
			page = requests.get(URL)
			if page.status_code == 200:
				soup = BeautifulSoup(page.content, 'html.parser')
				title_result = soup.find('h1', id='page-title', class_='title')
				#print(title_result.text.strip())
				div_result = soup.find('div', class_='jp-playlist')
				ul_result = div_result.find('ul')
				song_list = []
				li_result = ul_result.find_all('li')
				
				for i in li_result:
					 new_dict = {}
					 a_result = i.find('a')
					 link = a_result['href']
					 new_dict["title"] = a_result.text.strip()
					 new_dict["song_link"] = link
					 song_list.append(new_dict)
					 #print(link)
					 #print(a_result.text.strip(), end='\n'*2)
				album = {}   
				album["album_title"] = title_result.text.strip()     
				album["song_list"] = song_list
				album["page_url"] = URL
				pages_list.append(album)

	dawah_dict = {}
	dawah_dict['all'] = pages_list
	dawah_json_form = json.dumps(dawah_dict)
	print(dawah_json_form)
if __name__ == "__main__":
	main()