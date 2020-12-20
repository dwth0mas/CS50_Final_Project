import bs4
from urllib.request import urlopen as u_req
from bs4 import BeautifulSoup as Soup

red_rocks_url = "https://www.redrocksonline.com/events/"

u_client = u_req(red_rocks_url)
red_rocks_events_page_html = u_client.read()
u_client.close()

red_rocks_events_soup = Soup(red_rocks_events_page_html, "html.parser")

event_containers = red_rocks_events_soup.findAll("div", {"class": "card card-event event-month-active "
                                                                  "event-filter-active"})
print(event_containers[0])
container = event_containers[0]

# event_container_dates = event_containers.findAll("div", {"class": "date"})

for container in event_containers:
    print(container.find("div", {"class": "date"}).text.strip())
    print(container.find("h3", {"class": "card-title"}).text.strip())
    print(container.find("div", {"class": "buttons"}).text.strip())
    print("\n")
