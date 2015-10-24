#List Program
#LEVI WEISS

import random

#Ask user for two lists (.txt files)
print("Use this program to find the intersection or union of two .txt lists.")
user1 = input("Enter the filename of list1: ")
user2 = input("Enter the filename of list2: ")
afi_list = open(user1,"r")
rt_list = open(user2,"r")

#This is for testing purposes, directly loading in the txt file to save some time
##afi_list = open("top100moviesAFI.txt","r")
##rt_list = open("top100moviesRT.txt","r")

#Using readlines to read in each line of the txt file individually into a list
afi_set = set(afi_list.readlines())
rt_set = set(rt_list.readlines())

#the elements in common from the 2 lists
intersection = afi_set & rt_set

print("----------The two lists have these items in common----------")
for element in sorted(intersection):
    print(element.strip())

print()
#the union of the 2 lists
union = afi_set | rt_set
print("----------The two lists combined is----------")
for element in sorted(union):
    print(element.strip())
    
afi_list.close()
rt_list.close()

