from bs4 import BeautifulSoup 
import requests
import urllib.request
import os

def download(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	text = soup.find('h1').text
	#print(os.getcwd())
	#print(text)
	os.makedirs(text)
	image = [img for img in soup.find_all('img')]
	img_link = ['https://telegra.ph'+each.get('src') for each in image]
	#print(img_link)
	index=1
	for each in img_link:
		if (each[0:8]=='https://'):
			if(index<10):
				filename = text+'/0'+str(index)+'.jpg'
			else:	
				filename = text+'/'+str(index)+'.jpg'
			print(filename)
			urllib.request.urlretrieve(each, filename)
			index+=1

url = input("copy your url:")
download(url)