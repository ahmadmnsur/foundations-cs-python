import json
import requests
from bs4 import BeautifulSoup
lst_tabs=[]
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
def add_tab(title,url):
    new_tab={"title":title,"url":url,"nested":[]}
    lst_tabs.append(new_tab)   
def validate_index(tab,colse_or_switch):
        index=int(input("enter index "))
        if (index<len(tab)-1 and index<0) or index>len(tab)-1:
            if colse_or_switch=="close_tab":
                close_tab(tab,len(tab)-1)
            elif colse_or_switch=="switch_tab" :
                switch_tab(tab,len(tab)-1)
        else:
            if colse_or_switch=="close_tab":
                close_tab(tab, index)
            elif colse_or_switch=="switch_tab" :
                switch_tab(tab,index)     