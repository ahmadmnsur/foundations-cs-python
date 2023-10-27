#############   EX1


def count(x,d):
   if x>9  :
       
     x=(x//10)
     
     count(x,d+1)
   elif x<0:
     x=int(input("enter only positive number"))
     count(x,d)
    
   else:
      print(d)
     
#############   EX2
def find_max(lst):
    
  if len(lst)==1:
         return lst[0]
  max=find_max(lst[1:])
  if lst[0]>max:
         return lst[0]  
  else:
         return max  

 
###########  EX3
def count_tag(html, tag):
    open_tag = f"<{tag}>"
    close_tag = f"</{tag}>"
    open_tag_index = html.find(open_tag)
    close_tag_index = html.find(close_tag)
    
    
    if open_tag_index == -1 or close_tag_index == -1:
        return 0

    if open_tag_index<close_tag_index:
     return 1 + count_tag(html[close_tag_index + len(close_tag):], tag)
    else:
       return count_tag(html[close_tag_index + len(close_tag):], tag)
def menu():
  print("""1. Count Digits
2. Find Max
3. Count Tags
4. Exit""")
menu()
choice_menu=int(input("choice in this menu "))  
while choice_menu!=4:
 
  if choice_menu==1:
   x=int(input("enter number "))
   d=1
   count(x, d)
   menu()
   choice_menu=int(input("choice in this menu ")) 
   
  if choice_menu == 2:
   list = input("Enter a list of integers: ")
   list = [int(s) for s in list.split()]
   print(find_max(list))
   menu()
   choice_menu=int(input("choice in this menu ")) 
  if choice_menu==3:
    html_code = input("Enter the HTML code (multiline string):\n")
    tag_to_count = input("Enter the tag you want to count: ")

    count = count_tag(html_code, tag_to_count)
    print(f"The tag '{tag_to_count}' appears {count} times in the HTML code.")
    menu()
    choice_menu=int(input("choice in this menu "))
  if choice_menu==4:
     break

     
               