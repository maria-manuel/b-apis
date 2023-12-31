
# NOTE: With APIs, you are "at the whim" of the API provider, which means they
# can be shut down or changed with little warning. If you encounter such a
# problem with an API in this activity, be sure to let an instructor know!


import requests

print('------------ Challenge 1')
# Challenge 1
# Examine the following code. Can you understand what it is doing? As a
# hint, this is the code to use a Studio Ghibli API and fetch
# information about their films. Uncomment the print statement, and get
# it running.

##Outdated web address/API

# response = requests.get('https://ghibliapi.herokuapp.com/films/')
# data = response.json()
# # print(data)

response = requests.get('https://ghibliapi.vercel.app/films')
data = response.json()
print(data)

print('------------ Challenge 2')
# Challenge 2
# Write code to print out ONLY the "release_date" for "My Neighbor Totoro" from
# the list.
#
# Uncomment this code to get going.
#for item in data:
#    print(item['title'])

for item in data:
    if item['title'] == "My Neighbor Totoro":
        print(item['title'])
        print(item['release_date'])


print('------------ Challenge 3')
# Challenge 3
# Background: The European Central Bank provides real-time data on currency
# conversions. Read the API documentation for this Exchange Rates API:
#     https://kc-exchangeratesapi.herokuapp.com/
# Print out the following information:

# 1. All conversions between Euros and others
# 2. How many USD does one EUR buy today.
# 3. How many GPB does one EUR buy on the last day of 2015: 2015-12-31

# ####### MB Answer ###########
# response = requests.get('https://api.exchangeratesapi.io/latest')
# data = response.json()

# rates_dict = data['rates']
# for key, value in rates_dict.items():
#     print(key, value)

# print('US dollars for 1 EUR', rates_dict['USD'])
# response = requests.get('https://api.exchangeratesapi.io/2015-12-31?base=USD')
# data = response.json()

# rates_dict = data['rates']
# print('Euros for 1 USD', rates_dict)['EUR']

########## MM Answer ############

response = requests.get('https://api.exchangeratesapi.io/2015-12-31?base=USD')
data = response.json()
print(data['rates']['USD'])


print('------------ Challenge 4')
# NOTE: In 2021, the API used for this challenge has been off-and-on
# unavailable. Unfortunately there are no other free replacements, so if you
# are not getting any responses from it, feel free to skip these challenges,
# and instead skip to Challenge #6, a replacement challenge.

# Challenge 4
# DomainsDB.info is a site that looks up whether or not a domain name is
# registered.
# 1. Get it working using Python requests, and print the JSON results.
# 2. Try it out with other domain names
# 3. If you have extra time, can you figure out how to print ONLY the country
# that the domain was registered in? (and no other data)

# Hint: https://api.domainsdb.info/v1/domains/search?domain=ycombinator.com



print('------------ Challenge 5')
# Challenge 5
# Write a script that uses the Registered Domain Name Search API to look for
# *free domain* names with your first name, followed by the following words,
# followed by '.com'. For example, if your name was 'Joan', one might be
# 'joanhacker.com'.
#
# Hint: This is a tricky one! Experiment with different requests and see what
# results / errors / messages / etc you get back.

words = [
    'dev',
    'webdev',
    'pythonista',
    'coder',
    'hacker',
]




print('------------ Challenge 6')
# Challenge #6 - Replacing Challenge 4 & 5
# Open Library is a free book API, used to search for all types of information
# on published books.

# Here is a functioning REST API URL from openlibrary.org:
# http://openlibrary.org/search.json?q=earthsea&limit=10&offset=0
# Write code to do the following:
# - Search for your favorite book title or genre
# - Get a total of 15 results
# - Loop through the results, printing out the following information:
#      1. Title
#      2. Author(s)
#      3. Publish Year(s)




print('------------')
# Bonus Challenge
# (continues from "Replacement Challenge")
# Here is a functioning REST API URL from openlibrary.org:
# http://openlibrary.org/search.json?q=earthsea&limit=10&offset=0

# - Write a Python program that uses this API to search for a given book title
# based on user input
# - Create a system using "input" and "while" to allow the user to "flip"
# through "pages" of 4 results each


# Example Usage:
# $ python3 4_requests_marathon.py
# What search term? Hunger Games
# Hunger Games    - Page 1 of 24
# -
# 1980  -  Hunger by Patricia Houck Sprinkle
# 2018  -  Hunger Games by Catherine Driscoll, Alexandra Heatwole
# 2012  -  The Hunger Games by Suzanne Collins
# 2013  -  Hunger Games : l'Embrasement by Scholastic Canada Ltd
# ----------------------
# search, next, previous, quit? next
# -
# ----------------------
# Hunger Games    - Page 2 of 24
# -
# 2012  -  The Hunger Games by Kate Egan
# 2011  -  The hunger games companion by Lois H. Gresh
# 2013  -  Hunger Games, catching fire by Kate Egan
# 2010  -  Hunger Games: Mockingjay by Suzanne Collins
# ----------------------
# search, next, previous, quit? quit
# Goodbye!



print('------------')
# Advanced Bonus Challenge:
# Take a look at: https://github.com/public-apis/public-apis
# Which of those public APIs could you get working using requests?
# If you found any really cool ones, show them off!



