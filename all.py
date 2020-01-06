# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ("hi")

def hello():
    print("Hello, world!")

#%%
def myname():
    print("My name is Bill")
    
#%%
def ourschool():
    print("Coursera is our school")

#%%  
  
""" This will run forever. In this case Ctrl-C will stop it, but sometimes
that doesn't work. In that case, click away IP Console to stop; click yes to 
kill kernel. Open a new IPConsole on the Console menu to restart """
#%%
def forever():
    while True:
        pass
    
#%%
        ourschool()
        
#%%
from hashids import Hashids

pk = 123 # Your object's id
domain = 'imgur.com' # Your domain

hashids = Hashids(salt='this is my salt', min_length=6)
link_id = hashids.encode(pk)
url = 'http://{domain}/{link_id}'.format(domain=domain, link_id=link_id)
#%%
import hashlib
hashlib.md5("https://www.cisco.com/c/en/us/support/docs/asynchronous-transfer-mode-atm/operation-administration-maintenance-oam/117457-technote-cfm-00.html".encode('utf-8')).hexdigest()

#%%
import hashlib
hashlib.md5("https://www.cisco.com117457-technote-cfm-00.html".encode('utf-8')).hexdigest()[:8]

def main():

    file  = open('/Users/srinir/teams.txt', 'r').read()
    team  = input("Enter team name: ")
    count = file.count(team)

    print(count)

main()

#%%
import re 

logfile = open("/Users/srinir/warn.txt", "r") 

wordcount={}
for word in logfile.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
# print only the count for my_word instead of iterating over entire dictionary
#my_word="india"
#print (my_word, wordcount[my_word])
print(wordcount)

#%%

logfile = open("/Users/srinir/warn.txt", "r") 
my_word="lua"
count =0
for word in logfile.read().split():
    if my_word in word :
        count =count+1
        
print(count)
        
#%%



def find_second_largest(a):
    largest = 0;
    second_largest = 0;
    length = len(a)

    if length <2:
        return None

    for number in a:
        if largest < number:
            second_largest = largest
            largest = number
    #print(second_largest)
    return second_largest
            
def main():
    a=[1,3,2,4,5,7]
    b= [1]
    c=[1,2]
    print(find_second_largest(a))
    print(find_second_largest(b))
    print(find_second_largest(c))

main()

#%%
            
def main():
    a=[1,3,2,4,5,5,20]
    rightsum =0
    leftsum =0
    n = len(a)
    
    for elem in a:
        rightsum += elem
    #print(rightsum)
    
    for i in range(n-1, -1, -1) :
        leftsum += a[i]
        rightsum -= a[i]
        #print(rightsum,leftsum)
        
        if leftsum == rightsum:
            for k in range (0, i):
                print (a[k])
            print("--")   
            for k in range (i, n):
                print (a[k])
    
    return -1
        
main()


#%%
import subprocess

subprocess.getstatusoutput("ssh  127.0.0.2 'ls'")

#%%
import paramiko 

ssh = paramiko.SSHClient()
ssh.connect(server, username=username, password=password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)

#%%

def sort_with_dups (a, n):
    if n <=0 :
        print("invlaid input")
        return -1;
    a.sort()
    print(a)
    
def sort_with_dups_m (a, n):
    if n <=0 :
        print("invlaid input")
        return -1;
    
    print(a)    
    
def main():

    a=[2,3,5,11,0,0,3,2,1]
    sort_with_dups(a,len(a))

main()    
        
 #%%
def find_rotate_times(a):

    
    for i in range (0, len(a)-1):
        if a[i+1] - a[i] < 0:
            return i+1
def main():
    a=[6,7,8,9,10,1,2,3,4,5]
    b=[5,1,2,3,4]
    c=[1,2,3,4,5]
    d=[2,2,2,2,1,2]
    print(find_rotate_times(a))
    print(find_rotate_times(b))
    print(find_rotate_times(c))
    print(find_rotate_times(d))
    
main()    

#%%
def find_rotate_times(a):
    print(a, len(a))
    for i in range (0, len(a)-1):
        if a[i+1] - a[i] < 0:
            return i+1
    if i == len : 
        return 0
def main():
    a=[]
   
    T = int(input())
    
    for tests in range(0, T):
        nums = int(input())
        a = list(map(int, input().split()))
        print(find_rotate_times(a))
        #for i in range(0, nums):
            
           # elem = int(input())
            #a.append(elem)
            
    
    
   
    
main() 
#%%

"3" > "2"
"32" > "231"

#%%

a="string"
print(a.upper())
#%%
 a =True
print(int(a))

#%%
import os
print(os.walk(os.getcwd()))

#%%
def fib(n):
    fibo =[None]*n
    fibo[0]=1
    fibo[1]=1
    for i in range(2,n):
        fibo[i]=fibo[i-1]+fibo[i-2]
        print( fibo[i], i,fibo[i-1])
    return fibo[n-2]
fib(7)
    
#%%

word="112233444"

wordcount={}
for c in word:
    if c not in wordcount:
        wordcount[c] = 1
    else:
        wordcount[c] += 1
# print only the count for my_word instead of iterating over entire dictionary
#my_word="india"
#print (my_word, wordcount[my_word])
print(wordcount)
#%%

if __name__ == '__main__':
    
    word = input()
    wordcount =1
    count =0
    
for i in range(1, len(word)):
    if word[i-1] != word[i]:
        print("(",wordcount," ,",word[i],")", end=" ")
        wordcount = 1
    else:
        wordcount += 1
 # Enter your code here. Read input from STDIN. Print output to STDOUT1122
#%%
 myset = set([4,5,11,12])
 myset2 = set([4,5,33,44])
 print(myset.difference(myset2))
 print(myset2.difference(myset))
 
 mylist = list(myset.difference(myset2)) + list(myset2.difference(myset))

 mylist.sort()
 print(*mylist, sep="\n")
 
 #%%
 
import sys
import telnetlib

tn = telnetlib.Telnet("10.104.99.149")


tn.read_until(b"Username:", 2)
tn.write(b"admin\n")

tn.read_until(b"Password:", 2)
tn.write(b"########\n")

tn.read_until(b"CSR>", 2)
tn.write(b"show ip interface \n\n\n\n\n\n")
tn.write(b"exit\n")


str_all = tn.read_all()

f = open("output.txt", 'w')
f.write(str_all)

tn.close

#%%
