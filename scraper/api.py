from urllib import response
from bs4 import BeautifulSoup
import requests
import re

from scraper.models import News

def scrape(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    
    ranks = soup.find_all("span", class_="rank")

    titles = soup.find_all("a", class_="titlelink", href=True)
    details = soup.find_all("td", class_="subtext")

    for i in range(0, len(ranks)):
        title = titles[i].text
        link = titles[i]['href']

        score = details[i].find(text=re.compile('.*points')) if details[i].find(
            text=re.compile('.*points')) is not None else "0"
        author = details[i].find("a", class_="hnuser").text if details[i].find("a",
                                                                                class_="hnuser") is not None else ""
        comments = details[i].find(text=re.compile('.*(comments|comment)')) if details[i].find(
            text=re.compile('.*(comments|comment)')) is not None else "0"

        News.objects.create(title=title,link=link,points=int(score.split(" ")[0]),author=author,comments=int(comments.split("c")[0]))

def init():
    url = "https://news.ycombinator.com/news?=1"
    scrape(url)