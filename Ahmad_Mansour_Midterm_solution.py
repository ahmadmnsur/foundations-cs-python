import json
import requests
from bs4 import BeautifulSoup
def validate_url(add_or_open):
    try:
        title=input("enter title ").strip()
        url=input("enter url ").strip()
        requests.head(url,timeout=15)
    except requests.exceptions.RequestException:
        return print("url invalide")
    if add_or_open=="add_tab":
        return add_tab(title,url)
    if add_or_open=="open_nested_tab": 
        return open_nested_tab(title,url)