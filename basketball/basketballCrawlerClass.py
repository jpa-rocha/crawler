from bs4 import BeautifulSoup
from abstractClass.crawlerClass import Crawler
import basketball.Teams.Teams as full_teams


class BasketballCrawler(Crawler):
	def __init__(self, url):
		super().__init__(url)
	
		
	def find_data(self, league, year):
		path = ""
		if league == "nba":
			teams = full_teams.nba_teams
			path = "/teams"
		if self.get_page(path) != False:
			soup = BeautifulSoup(self.get_page(path), 'html.parser')

		links = set()
		for link in soup.find_all('a'):
			if link.get("href") is not None:
				for team in teams:
					if "teams/" + team[0]  + "/" + year in link.get("href"):
						links.add(link.get("href"))
			