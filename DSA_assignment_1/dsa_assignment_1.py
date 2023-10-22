#1 Write a program to find all pairs of an integer array whose sum is equal to a given number?
arr=[]
length= int(input("enter size of elements : "))
for i in range(length):
    num=int(input(f"enter the {i+1} th number : "))
    arr.append(num)
num= int (input("Enter number for pair : "))
def pairs(arr,num):
    pair=set()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==num:
                pa=(min(arr[i],arr[j]),max(arr[i],arr[j]))
                pair.add(pa)
    if not pair:
        print ("No Pairs found!",end=" ")
    else:
        return pair
print(pairs(arr,num))



# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def reverse(arr):
    left, right = 0, len(arr) - 1  
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
arr=[]
length= int(input("enter size of elements : "))
for i in range(length):
    num=int(input(f"enter the {i+1}th number : "))
    arr.append(num)
print(reverse(arr))


# Q3. Write a program to check if two strings are a rotation of each other?
string1=input("Enter string 1 : ")
string2=input("Enter string 2 : ")
def  rotatestring(str1,str2):
    if len(str1)!=len(str2):
        return False
    temp=str1+str2
    if str1 in temp:
        return True
    else:
        return False
    
if rotatestring(string1,string2):
    print("Yes! its rotation of each other")
else:
    print("No! its not a rotation of each other")


# Q4. Write a program to print the first non-repeated character from a string?

str1=input("Enter string : ")
def repeat(str)->str:
    temp={}
    for i in str:
        temp[i]=1+temp.get(i,0)
    for i in str1:
        if temp[i]==1:
            return i
print('1st Non-repeated character : ',repeat(str1))


# Q5. Write a recursive function to check if a given string is a palindrome.

string= input("Enter string : ")
def palindrome(string):
    if len(string)==1:
        return True
    if string[0]==string[-1]:
        return palindrome(string[1:-1])
    else:
        return False
print(palindrome(string))


# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
      
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  
        else:
            return None
    
    def get_stack(self):
        if not self.is_empty():
            return self.items
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def clearAll(self):
        self.items.clear()
        print("All Elements removed.")

string = input("Enter the postfix : ")
 
def postfix(string):
    res=''
    if len(string)<=1:
        return string
    else:
        stack=Stack()
        for strs in string:
            if strs in ["+",'-','*','/']:
                s1=stack.peek()
                stack.pop()
                s2=stack.peek()
                
                stack.pop()
                try:
                    res=strs+s2+s1+res
                except:
                    print ('Enter the valid postfix : ')
            else:
                stack.push(strs)
    return res
print('Prefix : ',postfix(string))


# Q7. Write a program to convert prefix expression to infix expression.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
      
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  
        else:
            return None
    

    def is_empty(self):
        return len(self.items) == 0

string = input("Enter the postfix : ")
 
def postfix(string):
    string=string[::-1]
    res=''
    if len(string)<=1 or string==None:
        return string
    else:
        stack=Stack()
        for strs in string:
            if strs in ["+",'-','*','/']:
                str = "(" + stack.pop() + f"{strs}" + stack.pop() + ")"
                stack.push(str)
            else:
                stack.push(strs)
    while not stack.is_empty():
        res+=stack.pop()
        
    return res 
print('Infix : ',postfix(string))



# Q8. Write a program to check if all the brackets are closed in a given code snippet.

def closed(string):
    temp={'(':0,')':0}
    for c in string:
        if c == "(" :
            temp['(']+=1
        if c==")":
            temp[')']+=1

        
    return temp['(']%2==0 and temp[')']%2==0

string = input('Enter the string : ')
print(closed(string))


# Q9. Write a program to reverse a stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
      
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  
        else:
            return None
    
    def get_stack(self):
        if not self.is_empty():
            return self.items
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def clearAll(self):
        self.items.clear()
        print("All elements removed.")

stack=Stack()
newstack=Stack()
lenth=int(input('Enter no of elements to Push : '))
for i in range(lenth):
    num=int(input(f"Enter {i+1}th number to append : "))
    stack.push(num)
print ('Original  Stack : ',stack.get_stack())
for i in range(lenth):
    stc=stack.get_stack()
    newstack.push(stc[lenth-(i+1)])
print ('New Stack : ',newstack.get_stack())



# Q10. Write a program to find the smallest number using a stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
      
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  
        else:
            return None
    
    def get_stack(self):
        if not self.is_empty():
            return self.items
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def clearAll(self):
        self.items.clear()
        print("All Elements removed.")

stack=Stack()
lenth=int(input('Enter no of elements to Push : '))
for i in range(lenth):
    num=int(input(f"Enter {i+1}th number to append : "))
    stack.push(num)
print ('Original  Stack : ',stack.get_stack())
print('Smallest number : ',min(stack.get_stack()))
