from scholarly import scholarly
from os.path import exists
import json

def pullData(): #pull data from API and store in dictionary and append to list
    unsortedList = []

    file = open("staffmembers.txt", "r")
    for line in file:
        line_split = line.split(',')
        search = line_split[1].strip()
        author = scholarly.search_author_id(search)
        pubs = scholarly.fill(author, sections=['publications'], publication_limit=10)

        for pub in author['publications']:
            info = scholarly.fill(pub, sortby="year")

            if("title" not in info['bib']):
                title = "No Title available."
            else:
                title = info['bib']['title']
            
            if("num_citations" not in info):
                num_citations = "No data available."
            else:    
                num_citations = info['num_citations']
        
            if("pub_url" not in info):
                url = "-"
            else:
                url = info['pub_url']

            if("author" not in info['bib']):
                author = "No data available."
            else:    
                author = info['bib']['author']

            if("pub_year" not in info['bib']):
                year = "0000"
            else:
                year = info['bib']['pub_year']

            if("abstract" not in info['bib']):
                abstract = "No abstract available."
            else:
                abstract = info['bib']['abstract']

            p = {"Title": title,
                "Num_Citations": num_citations,
                "URL": url,
                "Author": author,
                "Abstract": abstract,
                "Year": year
            }

            unsortedList.append(p)
        
    file.close()
    return unsortedList

def sortMostRecent(unsortedList =[]): #sort list according to most recently published
    most_recent = sorted(unsortedList, key=lambda p: int(p['Year']), reverse=True)

    return most_recent

def filelength():
    try:
        with open("most_recent.txt", "r") as file:
            filelist = file.readlines()
            length = len(filelist)
    except FileNotFoundError:
        with open("most_recent.txt", "w") as file:
            length = 0
            filelist = []
    return (length, filelist)

def checkFile(filelist, length,pub):          #checks if list of dictionaries is stored in file     
    if length == 0:
        return False
    else:
        match = False
        for iter in range(length):
            dict_str = filelist[iter]
            dctnry=json.loads(dict_str)
            if dctnry == pub:
                match = True

        if match == True:
            return True
        else:
            return False
    

def checkAppend(most_cited=[]):  #if file does not have one of the list entries, append missing entry to file.
    filelist = filelength()[1]
    length = len(filelength()[1])
    for x in most_cited:
        check = checkFile(filelist, length, x)
        if check == False:
            with open("most_recent.txt", "a") as file:
                file.write(json.dumps(x))
                file.write("\n")

def pullDataToFile(): #pulls data from API, sorts it and stores in most_cited.txt file
    unsortedList = []
    unsortedList = pullData()
    most_recent = sortMostRecent(unsortedList)
    checkAppend(most_recent)

def readFileToList(): #opens most_cited.txt file, stores data in list and returns the list
    most_recent = []
    with open("most_recent.txt") as file:
        lines = file.readlines()

    for line in lines:
        most_recent.append(json.loads(line))
    
    new_sort = sortMostRecent(most_recent)
    return new_sort

def checkFileExists():
    filepath = "most_recent.txt"
    file_exists = exists(filepath)
    return file_exists
""" --------------------------------------------------------------------------------------------------------------------------------------------------------"""
file_exists = checkFileExists()
if file_exists:
    most_recent = readFileToList()