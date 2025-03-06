def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def num_Words(file_contents):
    num_words = len(file_contents.split())
    return print(f"Found {num_words} total words")


def letter_count(file_contents):
    numOfTimes = {}
    count =1
    #Adds values to the dictionary
    for word in file_contents:
        letter = word.lower()
        if letter in numOfTimes:#if letter is present in the num of times dictionary
            numOfTimes[letter]+=count
        else:
            numOfTimes[letter]=count
    return numOfTimes

def sorted_list(dict):
    newList = []
    for k, v in dict.items():
        if k.isalpha():
            newList.append({"name": k, "num": v})
    return newList

def sort_on(dict):
    return dict["num"]


def final_sort(something):
    newDict={}
    something.sort(reverse=True, key=sort_on)
    for i in range(len(something)):
        for n, t in something[i].items():
            newDict[n] = t
        print(f"{newDict["name"]}: { newDict["num"]}")
    

    #Take dictionary numOfTimes, split its indexes, append the indexes to a new dictionarys(each index being a dictionary with keys of name and num), append all dictionaries to a list, sort list
   
