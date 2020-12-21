from urllib.request import urlopen
from bs4 import BeautifulSoup as Soup

red_rocks_url = "https://www.redrocksonline.com/events/"

u_client = urlopen(red_rocks_url)
red_rocks_events_page_html = u_client.read()
u_client.close()

red_rocks_events_soup = Soup(red_rocks_events_page_html, "html.parser")

event_containers = red_rocks_events_soup.findAll("div", {"class": "card card-event event-month-active "
                                                                  "event-filter-active"})

for container in event_containers:
    event_title = container.find("h3", {"class": "card-title"}).text.strip()
    event_date = container.find("div", {"class": "date"}).text.strip()
    ticket_link = container.find("a", {"class": "btn btn-white small"})['href']

    print(event_title)
    print(event_date)
    print(ticket_link)
    print("\n")
