from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
