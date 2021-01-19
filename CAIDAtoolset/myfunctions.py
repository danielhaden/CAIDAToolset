import urllib.request
from bs4 import BeautifulSoup
import re

def list_datasets(self):
    '''
    Returns a list of all available IDTKs from CAIDA's Ark infrastructure.
    '''

    page = urllib.request.urlopen(self.CAIDA_ROOT_URL)

    htmlBytes = page.read()
    html = htmlBytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    for a in soup.find_all('a', href=True):
        match = re.search("[0-9]*", a['href'])
        if match.group(0) != "":
            print(a['href'])