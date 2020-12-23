from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as Soup
import sqlite3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Creating a database connection
sqliteConnection = sqlite3.connect("denver_shows.sqlite", check_same_thread=False, isolation_level=None)
db = sqliteConnection.cursor()

