from scholarly import scholarly
from os.path import exists
import json


def pullData(): #pull data from API and store in dictionary and append to list
    authorList = []

    file = open("staffmembers.txt", "r")
    for line in file:
        line_split = line.split(',')
        search = line_split[1].strip()
        author = scholarly.search_author_id(search)
        info = scholarly.fill(author)

        #scholarly.pprint(info)
        if ("name" not in info):
            name = line
        else:
            name = info['name']

        if ("affiliation" not in info):
            aff = "No affliations available."
        else:
            aff = info['affiliation']

        if ("homepage" not in info):
            homepage = "----"
        else:
            homepage = info['homepage']

        if ("interests" not in info):
            interests = "None"
        else:
            interests = info['interests']

        if ("scholar_id" not in info):
            scholarid = "----"
        else:
            scholarid = info['scholar_id']

        if ("url_picture" not in info):
            pic = "----"
        else:
            pic = info['url_picture']

        a = {"Name": name,
            "Affiliations": aff,
            "Homepage": homepage,
            "Interests": interests,
            "Scholar": scholarid,
            "Pic": pic
        }

        authorList.append(a)
        
    file.close()
    return authorList

def sortAlphabet(authorList =[]): #sort list according to last name in ascending order
    newList = sorted(authorList, key=lambda a: (a['Name'].split(" ")[-1]))

    return newList

def filelength():
    try:
        with open("authors.txt", "r") as file:
            filelist = file.readlines()
            length = len(filelist)
    except FileNotFoundError:
        with open("authors.txt", "w") as file:
            length = 0
            filelist = []
    return (length, filelist)

def checkFile(filelist, length, d):          #checks if list of dictionaries is stored in file     
    if length == 0:
        return False
    else:
        match = False
        for iter in range(length):
            dict_str = filelist[iter]
            dctnry=json.loads(dict_str)
            if dctnry == d:
                match = True

        if match == True:
            return True
        else:
            return False

def checkAppend(sortedList=[]):  #if file does not have one of the list entries, append missing entry to file.
    filelist = filelength()[1]
    length = len(filelength()[1])
    for x in sortedList:
        check = checkFile(filelist, length, x)
        if check == False:
            with open("authors.txt", "a") as file:
                file.write(json.dumps(x))
                file.write("\n")

def pullDataToFile(): #pulls data from API, sorts it and stores in authors.txt file
    authorList = []
    authorList = pullData()
    sortedList = sortAlphabet(authorList)
    checkAppend(sortedList)

def readFileToList(): #opens authors.txt file, stores data in list and returns the list
    authorList = []
    with open("authors.txt") as file:
        lines = file.readlines()

    for line in lines:
        authorList.append(json.loads(line))
    
    new_sort = sortAlphabet(authorList)
    return new_sort

def checkFileExists():
    filepath = "authors.txt"
    file_exists = exists(filepath)
    return file_exists
""" -------------------------------------------------------------------------------------------------------------------------"""
file_exists = checkFileExists()
if file_exists:
    authorList = readFileToList()
