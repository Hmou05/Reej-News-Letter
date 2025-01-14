from requests import get
from bs4 import BeautifulSoup as bs
import lxml

url = "https://intellij-support.jetbrains.com/hc/en-us/community/posts/"
re = get(url)
source = re.content
print(re.status_code)
soup = bs(source, "lxml")

container = soup.findAll("div", {"class": "article-content"})
print(len(container))