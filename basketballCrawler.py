from basketball.basketballCrawlerClass import BasketballCrawler

basketball = BasketballCrawler("https://www.basketball-reference.com/")
basketball.crawl_data("nba", "2023")