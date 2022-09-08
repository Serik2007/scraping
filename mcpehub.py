import requests
from bs4 import BeautifulSoup
import lxml
import csv


def get_data(max_page):
	

	z = 1


	while z < int(max_page):

		response = requests.get(url=f'https://mcpehub.org/mods/page/{z}/')
		soups = BeautifulSoup(response.text, 'lxml').find_all('article', class_='col-xs-12 col-sm-4 col-md-6')


		for soup in soups:
			

			link = soup.find('a', class_='news-item border-radius').get('href')

			
			response_L2 = requests.get(link)
			soup_L2 = BeautifulSoup(response_L2.text, 'lxml')


			name_addon = soup_L2.find('h1', attrs={'itemprop': 'headline'}, class_='bold black').text
			photo_url = soup_L2.find('div', class_='fullstory-image').find('img').get('src')
			views = soup_L2.find('span', class_= 'format-numb').text
			comments = soup_L2.find_all('span', class_= 'format-numb')[-1].text
			date = soup_L2.find('span', class_='date regular transparent-grey').text
			download_links_step_1 = soup_L2.find_all('div', class_='content-box')


			link = ''
			for links in download_links_step_1:
				link += (links.find('a', class_='flex middle center green-bg medium white').get('href')) + ', '


			#if you need to save in csv
			#save_as_csv(name_addon = name_addon, photo_url=photo_url, views=views, comments=comments, date=date, link=link) #recomment this
		z+=1
def save_as_csv(name_addon, photo_url, views, comments, date, link):
	

	with open('mcpehub.csv', 'a', encoding='utf-8') as file:
		writer = csv.writer(file)
		writer.writerow(
			[
			name_addon,
			photo_url,
			views,
			comments,
			date,
			link
			]
			)

def main():
	get_data()

if __name__ == '__main__':
	main()
	print('Created by Cerik')