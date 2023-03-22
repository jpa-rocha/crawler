from abc import (
	ABC,
	abstractmethod,
)

from urllib import (
	request
)

import os

class Crawler(ABC):
	def __init__(self, url):
		self.url = url
		
	def check_url(self, url):
		try:
			check = request.urlopen(self.url + url)
			return True
		except:
			print(f"No page exists at: {self.url + url}")
			return False
	
	def get_page(self, url):
		if self.check_url(url) == True:
			check = request.urlopen(self.url + url).read()
			return check
		else:
			return False


	def create_folder(self, name):
		if not os.path.exists(name):
			os.makedirs(name)
			print(f"Folder {name} created.")
		else:
			print(f"Folder {name} already exists.")


	def navigate(self, url):
		if self.check_url(url) == True:
			check = request.urlopen(self.url + url).read()
			return check
		else:
			return False

	@abstractmethod
	def find_data(self):
		pass
