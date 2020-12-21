from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as Soup

gothic_events_url = "https://www.gothictheatre.com/events/rescheduled"

req = Request(gothic_events_url, headers={'User-Agent': 'Mozilla/5.0'})
u_client = urlopen(req)
gothic_events_page_html = u_client.read()
u_client.close()

gothic_events_soup = Soup(gothic_events_page_html, "html.parser")

event_containers = gothic_events_soup.findAll("div", {"class": ["entry gothictheatre clearfix",
                                                                "entry alt gothictheatre clearfix"]})

for container in event_containers:
    event_title = container.find("h3", {"class": "carousel_item_title_small"}).text.strip()
    event_date = container.find("span", {"class": "date"}).text.strip()
    event_time = container.find("span", {"class": "time"}).text.strip()
    ticket_link = container.find("a", {"title": "Get Tickets"})['href']

    event_time_start_substring = (len(event_time) - 7)
    event_time_end_substring = len(event_time)

    print(event_title)
    print(event_date)
    print(event_time[event_time_start_substring:event_time_end_substring])
    print(ticket_link)
    print("\n")