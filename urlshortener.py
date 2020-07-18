import pyshorteners

#you need to be connected to the internet.
#install the pyshorteners library (pip install pyshorteners or pip3 install pyshorteners) in your terminal

url=input("Please input your url: \n")

print("The Shortened URL is:", pyshorteners.Shortener().tinyurl.short(url))