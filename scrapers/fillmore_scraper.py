from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as Soup

fillmore_events_url = "http://www.fillmoreauditorium.org/events/"

req = Request(fillmore_events_url, headers={'User-Agent': 'Mozilla/5.0'})
u_client = urlopen(req)
fillmore_events_page_html = u_client.read()
u_client.close()

fillmore_events_soup = Soup(fillmore_events_page_html, "html.parser")

event_containers = fillmore_events_soup.findAll("li", {"class": "em-entry-list-item"})

for container in event_containers:
    event_title = container.find("h3", {"class": "em-entry-title"}).text.strip()
    event_date = container.find("time", {"class": "em-entry-time"})['datetime']
    ticket_link = container.find("a", {"class": "em-entry-cta-link"})['href']

    print(event_title)
    print(event_date[0:10])
    print("http://www.fillmoreauditorium.org" + ticket_link)
