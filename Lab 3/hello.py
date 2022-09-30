#!/usr/bin/env python3

import os
import json

#PRINT ALL ENVIRONMENT VARIABLES AS A PLAIN TEXT

#print("Content-Type: text/plain") #let browser know to expect plain text
#print()
#print(os.environ)

#PRINT ENV VARIABLES AS JSON

print("Content-Type: application/json") #let browser know to expect json
print()
print(json.dumps(dict(os.environ), indent=2)) #print w/ nice formatting

#PRINT QUERY PARAMTER DATA IN HTML

#print("Content-Type: text/html") #let browser know to expect html
#print()
#print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")
