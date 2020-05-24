import requests
from bs4 import BeautifulSoup

def ShowCategories():
	categories = ["All", "India", "Business", "Sports", "World", "Politics",
				"Technology", "Startup", "Entertainment", "Miscellaneous",
				"Hatke", "Science", "Automobile"]
	print(categories)
				
def InshortAPI(category=""):
	if category == "All":
		category=""
	newsDictionary = []		
	htmlBody = requests.get('https://www.inshorts.com/en/read/' + category)
	soup = BeautifulSoup(htmlBody.text, 'lxml')

	newsCards = soup.find_all(class_='news-card')

	for card in newsCards:
		try:
			title = card.find(class_='news-card-title').find('a').text
			imageUrl = card.find(class_='news-card-image')['style'].split("'")[1]
			url = ('https://www.inshorts.com' + card.find(class_='news-card-title').find('a').get('href'))
			content = card.find(class_='news-card-content').find('div').text
			author = card.find(class_='author').text
			date = card.find(clas='date').text
			time = card.find(class_='time').text
			readMoreUrl = card.find(class_='read-more').find('a').get('href')
			newsObject = {
				"title": title,
				"imageUrl": imageUrl,
				"url": url,
				"content": content,
				"author": author,
				"date": date,
				"time": time,
				"readMoreUrl": readMoreUrl
		}
			newsDictionary.append(newsObject)

		except:
			pass
			
	return newsDictionary

def main():
	newsDictionary = inshortAPI("Miscellaneous")
	for x,y in newsDictionary[0].items():
		y = y.replace("\n","")
		print(f"{x} - {y}",end="\n\n")
	ShowCategories()

if __name__ == '__main__':
	main()


		
