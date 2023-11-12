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
    try:
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
    except ValueError:
        print("please enter only integer number")
def close_tab(tab,index):
    if len(tab)>0:
        tab.pop(index)
    else:
        print("There is no tab to close it")         
def switch_tab(tab,index):
    if len(tab)>0:
        page =requests.get(tab[index]["url"])
        src=page.content               # byte code
        soup=BeautifulSoup(src,"lxml")  # parsing
        print(soup)
    else:
        print("There is no tab")
def display_all_tabs(tabs):
    if len(tabs)>0:
        for parent in range(len(tabs)):
            print(tabs[parent]["title"])
            if len(tabs[parent]["nested"])>0:
                for nested in range(len(tabs[parent]["nested"])):
                    allnesteds=""
                    allnesteds+=tabs[parent]["nested"][nested]["title"]
                    print("  nested tab: " ,allnesteds )
def open_nested_tab(title_nested,url_nested):
    try:
        index_nested=int(input("enter the index of the parent tab to insert additional tab: "))
        if  index_nested<len(lst_tabs) and index_nested>=0 :
            nested_tab={"title":title_nested,"url":url_nested}
            lst_tabs[index_nested]["nested"].append(nested_tab)
        else:
            print("number of index out of bound")
    except ValueError:   
        print("index should be only integer number")          
def clear_all_tabs(_lst_tabs):
    _lst_tabs.clear()
def save_tabs(_lst_tabs):
    file_path=input("Enter the file path to save the tabs: ").strip()
    if not file_path.endswith(".json"):
        print("please enter a json file format ")
    elif len(file_path[:-5])>0:
        with open(file_path,"a") as  convert_format:
            convert_format.write(json.dumps(_lst_tabs,indent=2))
def import_tabs():
    try:
        file_path=input("Enter the file path to import the tabs: ").strip()
        if not file_path.endswith(".json"):
            print("please enter a json file format ")
        elif len(file_path[:-5])>0:
            with open(file_path,"r",encoding="utf-8") as read_file:
                read=json.load(read_file)
                print(read)
    except FileNotFoundError:
        print("please enter the correct file name")
 def main():
        print("Menu:")
        print("1. Open Tab")
        print("2. Close Tab")
        print("3. Switch Tab")
        print("4. Display All Tabs")
        print("5. Open Nested Tab")
        print("6. Clear All Tabs")
        print("7. Save Tabs")
        print("8. Import Tabs")
        print("9. Exit")
        choice = int(input("Enter your choice: "))
        if (choice)==1:
            validate_url("add_tab")
        elif (choice)==2:
            validate_index(lst_tabs,"close_tab")
        elif (choice)==3:
            validate_index(lst_tabs,"switch_tab")
        elif choice==4:
            display_all_tabs(lst_tabs)
        elif choice==5:
            validate_url("open_nested_tab")
        elif choice==6:
            clear_all_tabs(lst_tabs)
        elif choice==7:
            save_tabs(lst_tabs)
        elif choice==8:
            import_tabs()                    
            