from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as Soup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def red_rocks_scraper():
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


def ogden_scraper():
    ogden_events_url = "https://www.ogdentheatre.com/events/rescheduled"

    req = Request(ogden_events_url, headers={'User-Agent': 'Mozilla/5.0'})
    u_client = urlopen(req)
    ogden_events_page_html = u_client.read()
    u_client.close()

    ogden_events_soup = Soup(ogden_events_page_html, "html.parser")

    event_containers = ogden_events_soup.findAll("div", {"class": ["entry ogden clearfix", "entry alt ogden clearfix"]})

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


def mission_scraper():
    mission_events_url = "https://www.missionballroom.com/upcoming-events/"

    chrome_options = Options()
    chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options,
                              executable_path='/Users/dthomas/Documents/PycharmProjects/CS50_Final_Project/drivers'
                                              '/chromedriver_mac_87')
    driver.get(mission_events_url)

    mission_events = driver.find_elements_by_class_name('event-wrap')

    for event in mission_events:
        event_title = event.find_element_by_xpath('.//*[@class="event-title"]')
        event_date = event.find_element_by_xpath('.//*[@class="event-date"]')
        ticket_link = event.find_element_by_xpath('.//*[@class="btn btn-dark ticket-link"]').get_attribute('href')

        print(event_title.text)
        print(event_date.text)
        print(ticket_link)

    driver.close()


def fillmore_scraper():
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


def gothic_scraper():
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
