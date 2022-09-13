import requests

print(requests.__version__)
r = requests.get('https://www.google.com/')
r1 = requests.get('https://raw.githubusercontent.com/harkiratmalhi/CMPUT404-Lab-1/master/question2_lab1.py').content
print(r1)
