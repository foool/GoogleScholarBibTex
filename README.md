# GoogleScholarBibTex
Script to batch get BibTeXs of papers collected in your Google Scholar library.

## required packages
> * Requests ,  http://www.python-requests.org/
> * BeautifulSoup4, https://www.crummy.com/software/BeautifulSoup/

## Tips
> * The script only print the BibTeX of each paper, you can put all contents in a `bib` file with the conmmand `python GoogleScholarBibtex > google.bib`
> * Google could ban your visit temporarily if you access Google frequently in a short time.  

## Errors
> * If you meet a `SSLError`as follow: `requests.exceptions.SSLError: hostname 'scholar.google.com' doesn't match 'www.google.com'`, please get more informations from http://docs.python-requests.org/en/master/community/faq/#what-are-hostname-doesn-t-match-errors. The fast way to fix this problem is to upgrade your Python to 2.79+ or Python3. 
