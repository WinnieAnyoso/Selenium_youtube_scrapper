from selenium import webdriver

Youtube_trending_url = "https://www.youtube.com/feed/trending"

driver = webdriver.Chrome()

driver.get(Youtube_trending_url)

print('Page title :', driver.title)
