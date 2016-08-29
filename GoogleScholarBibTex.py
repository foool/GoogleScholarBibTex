#_*_coding:utf-8_*_

try:
	import requests
except Exception:
	print "You should install requests. http://www.python-requests.org/"
import os
import sys
try:
	from bs4 import BeautifulSoup
except Exception:
	print "You should install BeautifulSoup4. https://www.crummy.com/software/BeautifulSoup/"
import re

# change 'INPUT YOUR GOOGLE ACCOUNT HERE' to your google account
google_account = "INPUT YOUR GOOGLE ACCOUNT HERE"
# change "INPUT YOUR GOOGLE PASSWORD HERE" to you google password
google_password = "INPUT YOUR GOOGLE PASSWORD HERE"

url_login = "https://accounts.google.com/ServiceLogin"
url_auth = "https://accounts.google.com/ServiceLoginAuth"
# maximum pages in your library
max_pages = 100	

class SessionGoogle:
    def __init__(self, url_login, url_auth, login, pwd):
        self.ses = requests.session()
        login_html = self.ses.get(url_login)
        soup_login = BeautifulSoup(login_html.content, 'html.parser').find('form').find_all('input')
        dico = {}
        for u in soup_login:
            if u.has_attr('value'):
                dico[u['name']] = u['value']
        # override the inputs with out login and pwd:
        dico['Email'] = login
        dico['Passwd'] = pwd
        self.ses.post(url_auth, data=dico)

    def get(self, URL):
        return self.ses.get(URL).text.encode('utf-8')

if __name__ == '__main__':
    session = SessionGoogle(url_login, url_auth, google_account, google_password)
    content = session.get("https://scholar.google.com/")
    for i in xrange(max_pages):
	ii = i*10
	page_url = "https://scholar.google.com/scholar?start=%d&hl=en&as_sdt=0,5&scilib=1"%ii
	con = session.get(page_url)
	p = re.compile("return gs_ocit\(event,'(\w+)'")
	allinfos = p.findall(con)
	if len(allinfos) == 0:
		exit()
	for pinfo in allinfos:
		pinfo_url = "https://scholar.google.com/scholar?scila=%s&output=cite&hl=en"%pinfo
		pinfo_con = session.get(pinfo_url)
		p = re.compile("(https://scholar.googleusercontent.com/.+?)\">BibTeX<")
		bib_url = p.findall(pinfo_con)
		if len(bib_url) < 1:
			#print "Cannot find BibTeX of the paper"
			continue
		bib_url = bib_url[0].replace('&amp;','&')
		bib_con = session.get(bib_url)
		# Output the BibTex of each paper
		print bib_con
