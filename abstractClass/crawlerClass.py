from abc import (
	ABC,
	abstractmethod,
)

from urllib import (
	request
)

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

	@abstractmethod
	def find_data(self):
		pass
