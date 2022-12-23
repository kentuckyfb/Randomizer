from turtle import clear
import random
import re

import sys
#recursion limit increased for finding longest full name using recursion
sys.setrecursionlimit(10000)

#create list of full names using two given lists
def create(fn, ln):
        #emtpy list to store full names
        fullnames = []
        #get firstname
        for first in fn:
            fullnames.append(first)
        #get lastname
        for last in range(len(ln)):
            fullnames[last] = fullnames[last] + " " + ln[last]

        return fullnames
    
#find longest full name in list using recursion
def longest_Recursion(arr):
        #base case: when array only contains one item
        if(len(arr) == 1):
            return arr[0]
        #recursive call with sliced array 
        k = longest_Recursion(arr[1:])
        #check length of returned arr item and current array item and return the largest
        if(k.__len__() >= arr[0].__len__()):
            return k
        else:
            return arr[0]

#find longest full name in list using iteration
def longest_Iteration(arr):
        #varaible to store largest name
        cur = ''
        #iterate through the array
        for i in arr:
            #compare lengths 
            if(len(cur) < len(i)):
                cur = i
        return cur

#function to write into a text file
def writeToFile(filename, text):
    #open text file in write mode
    file = open(filename, "w") 
    #loop to iterate through text
    for i in text:
        #concatanate \n for new line and write 
        i = i + "\n"
        file.writelines(i)
    file.close()

#class for file handling
class files:
    filename = ""
    wordlimit = 0
    full_list = []
    num_lines = 0

    def __init__(self, filename, wordlimit):
        self.filename = filename
        self.wordlimit = wordlimit

    #get full list
    def get_full_list(self):
        return self.full_list

    #get filename
    def get_filename(self):
        return self.filename

    #get specified word limit
    def get_wordlimit(self):
        return self.wordlimit

    #set specific word limit
    def set_wordlimit(self, wordlimit):
        self.wordlimit = wordlimit

    #gets number of items in full list before trim
    def get_full_list_num(self):
        return len(self.full_list)

    #gets number of lines in text file
    def get_lines(self):
        files.set_lines(self)
        return self.num_lines

    #shuffles items in list
    def shuffle(self):
        random.shuffle(self.full_list)

    #reads text file
    def readfile(self):
        #open file
        file = open(self.filename, "r")

        #put elements to a list line by line
        self.full_list = file.readlines()
        print("number of lines in " + self.filename + " : " + str(len(self.full_list)))
        file.close()

    #trimming words in list to word limit
    def trim(self):
        #trim words to word limit
        list = self.get_full_list()
        trimmed_list = []
        for word in list[0:self.get_wordlimit()]:
            trimmed_list.append(word)
        return trimmed_list

    #writing trimmed 4000 names into a text file
    def writeTofile(self, filename, list):
        #open file in wirting mode
        file = open(filename, "w") 
        for i in list:
            file.write(i)
        file.close()

maxval = 4000
#storing first names
firstname = files("firstName.txt", maxval)
firstname.readfile()
firstname.shuffle()
fn = firstname.trim()
firstname.writeTofile("trimmed_firstName.txt", fn)

#sorting last names
lastname = files("lastName.txt",maxval)
lastname.readfile()
lastname.shuffle()
ln = lastname.trim()
lastname.writeTofile("trimmed_lastName.txt", ln)

#making full names
list = create(fn, ln)

#formatting full names
list2 = []
for item in list:
    item2 = item.replace('\n', '')
    list2.append(item2)

writeToFile("fullNames.txt", list2)

#recursion
name = longest_Recursion(list).replace('\n', '')
print("Longest name in list using Recursion : " + name + " \nlength: " + str(len(name)))

#iteration
name = longest_Iteration(list).replace('\n', '')
print("Longest name in list using Iteration : " + name + " \nlength: " + str(len(name)))
