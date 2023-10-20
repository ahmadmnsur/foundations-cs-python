## Exercixe one
def factorial ():
    
    while True:
     
      inp=input("enter a positive integer: ")
      try:
       val=int(inp) 
       if val<0 :
        print("factorial doesnot exist for negative number")
        return factorial()
       elif val==0:
          print(1) 
       else: 
          fact=1
          for i in range (1,val+1):
            fact*=i
       break
      except ValueError: 
       print("please don't enter a string or float number")       
    print(fact)
    
  
 ##############################################  

#############      Exercice 2      ##########################
def find_divisors():
   
   while True:
     try:  
      divisors=[]
      input_divisors=int(input("enter an integer ")) 
      if input_divisors<0:
         print("enter only positive number")
         return find_divisors()
   
      for ii in range(1,input_divisors+1):
        if (input_divisors%ii)==0:
            divisors.append(ii)
      print(f"divisors of {input_divisors} is {divisors}")  
      break
     except ValueError:
         print("please don't enter a string or float number")
         
############################################################# 
#############      Exercice 3      ##########################

def reverseString(string_reverse): 
  empty_string=""
  for y in range(len(string_reverse)-1,-1,-1):
     empty_string+=string_reverse[y]
  return empty_string 

############################################################# 
#############      Exercice 4      ##########################

def even():
   input_even=input("Enter a list of integers separated by spaces:")
   list_even=[]
   try:
      list_check=[int (check) for check in input_even.split()]
      for number in list_check:
         if number%2==0:
            list_even.append(number)
      print(list_even)      
   except ValueError:
      print("please enter only number separated by spaces")
      even()

############################################################# 
#############      Exercice 5      ##########################

def password():
 a =input("type the password a ")
 count_num=0
 count_special=0 
 count_upper=0
 for i in range (0,len(a),1):
   if a[i].isnumeric():
     count_num+=1
 if count_num <1:
         return False
 
 for ii in range (0,len(a),1): 
    if a[ii].isupper():
        count_upper+=1 
 if count_upper<1: 
         return False

 for iii in range(0,len(a)):
    if a[iii]=="!" or  a[iii] =="@" or a[iii]=="$" or a[iii]=="#" :
       count_special+=1
 if count_special<1: return False
       
 if count_special>=1 and count_upper>=1 and count_num>=1 and len(a)>=8:
    if len(a)>15:
        print("is to large") 
        password()
    return True    
  

############################################################# 
#############      Exercice 6      ##########################  

def ipv4():
    user_input = input("Enter an IPv4 address: ")
    octets = user_input.split('.')
    
    if len(octets) != 4:
        return False
    
    for octet in octets:
      
        if octet !="0" and octet.startswith("0"):
             return False
         
        if not octet.isdigit():  
            return False
        value = int(octet)  
        if value < 0 or value > 255: 
            return False

    return True
   
def main(): 
    print("__________Exercice 1_________\n")
    factorial()
    print("\n__________Exercice 2_________")
    find_divisors()
    print("\n__________Exercice 3_________")
    string_reverse=input("enter a string: ")
    print(reverseString(string_reverse))
    print("\n__________Exercice 4_________")
    even()
    print("\n__________Exercice 5_________")
    if password():
     print("strong")
    else:
     print("weak")
    print("\n__________Exercice 6_________")
    if ipv4():
     print("Valid IPv4 address")
    else:
     print("Invalid IPv4 address")    

main()    