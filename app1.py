#!/usr/bin/env python3

import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def convert(w):
 w = w.lower()
 if w in data:
  return data[w]
 elif len(get_close_matches(w,data.keys()))>0:
  yn=input("did u mean %s instead?[Y/N]" % get_close_matches(w,data.keys())[0])
  if yn == "y":
   return data[get_close_matches(w,data.keys())[0]]
  else:
   return "go to hell"
 else:
  return "word doesn't exist..please recheck..."

word=input("\nenter the word: ")

op=convert(word)

if type(op) == list:
 for i in op:
  print("\n %s \n" %i)

else:
 print(op)
 
