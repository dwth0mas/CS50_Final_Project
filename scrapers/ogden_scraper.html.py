import bs4
from urllib.request import urlopen as u_req, Request
from bs4 import BeautifulSoup as Soup

ogden_events_url = "https://www.ogdentheatre.com/events/rescheduled"

req = Request(ogden_events_url, headers={'User-Agent': 'Mozilla/5.0'})
u_client = u_req(req)
ogden_events_page_html = u_client.read()
u_client.close()

ogden_events_soup = Soup(ogden_events_page_html, "html.parser")

# print(ogden_events_soup)

event_containers = ogden_events_soup.findAll("div", {"class": ["entry ogden clearfix", "entry alt ogden clearfix"]})
print(event_containers)

for container in event_containers:
    print(container.find("h3", {"class": "carousel_item_title_small"}).text.strip())
    print(container.find("span", {"class": "date"}).text.strip())
    print(container.find("span", {"class": "time"}).text.strip())
    print(container.find("div", {"class": "buttons"}))
    print("\n")
