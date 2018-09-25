import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib

url = "https://transponder.tv/login"
channellist = "https://transponder.tv/channels/"
provider = "https://transponder.tv/watch/"
channels = []

cj = cookielib.CookieJar()
login = mechanize.Browser()
login.set_handle_robots(False)
login.set_cookiejar(cj)
login.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
login.open(url)

login.select_form(nr=0)
login.form['email'] = 'USERNAME'
login.form['password'] = 'PASSWORD'
login.submit()

list = mechanize.Browser()
list.set_handle_robots(False)
list.set_cookiejar(cj)
list.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
list.open(channellist)
all = BeautifulSoup(list.response().read())


for listall in all.find_all('div', class_='primaryBubble'):
 for a in listall.find_all('a'):
  channels = a.get('href')
  print channels

chan = raw_input("Please enter channel name : ")

scrape = mechanize.Browser()
scrape.set_handle_robots(False)
scrape.set_cookiejar(cj)
scrape.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
scrape.open(provider + chan)
beaut = BeautifulSoup(scrape.response().read(), "lxml")
TV = beaut.find("source").get("src")
print TV






