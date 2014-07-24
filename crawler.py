#!/usr/bin/env python

import sys, requests, re
from BeautifulSoup import BeautifulSoup

def get_links_from(page) :
	html = requests.get(page)
	page = BeautifulSoup(html.text)
	links = page.findAll('a', attrs={'href': re.compile("^http://")})
	return links

page = sys.argv[1]
depth = int(sys.argv[2])

links = get_links_from(page)

while depth :
	tmp = []
	print "----------- LEVEL=" + str(depth) + "-----------"
	for link in links :
		print ">> " + link['href']
		tmp += get_links_from(link['href'])
	links = tmp
	tmp = []
	depth -= 1
