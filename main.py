from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/read_book/{item_book}")
def read_book(item_book):
    item_book = int(item_book)
    if(item_book==int(1)):
        print("Get mary shellybook");
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            words = file_contents.split()
            numberwords = len(words)
            dict=count_character(words)
            report(dict)
            return numberwords,dict
    else:
        print("Adios");

def count_character(words):
    print("Make a function to count characteres")
    dict = {}
    for w in words:
        w = w.lower()
        for l in w:
            try:
                if l in dict.keys():
                    dict[l]=dict[l]+1
                else:
                    dict[l]=1
            except:
                print("error")
    return(dict)

def report(dict):
    for key, value in dict.items():
       print("The ",key," character was found ",value," times")