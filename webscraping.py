"""
    Web Scraping

Author: Ana M. Almeida
Date: 28.09.2022

Guide: https://github.com/anamvalmeida/courses/blob/Applied-AI/WebScraping_v2.ipynb
"""

from bs4 import BeautifulSoup # This module helps in web scrapping.
import requests  # This module helps us to download a web page.

# BEAUTIFUL SOUP OBJECTS
print('BEAUTIFUL SOUP OBJECTS')
print(' ')

# Beautiful Soup is a Python library for pulling data out of HTML
# and XML files, we will focus on HTML files. This is accomplished
# by representing the HTML as a set of objects with methods used to
# parse the HTML. We can navigate the HTML as a tree and/or filter
# out what we are looking for.

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
print('HTML:',html)
print(' ')

# To parse a document, pass it into the BeautifulSoup constructor,
# the BeautifulSoup object, which represents the document as a nested
# data structure:
soup = BeautifulSoup(html, "html.parser")
print('Soup:',soup)
print(' ')

# Beautiful Soup transforms a complex HTML document into a complex
# tree of Python objects. The BeautifulSoup object can create other
# types of objects.

# We can use the method prettify() to display the HTML in the nested structure:
print('Soup (prettify):')
print(soup.prettify())
print(' ')

#  The Tag object corresponds to an HTML tag in the original document,
# for example, the tag title.
tag_object = soup.title
print('Tag Object Title:',tag_object)
print('Tag Object Title (type):',type(tag_object))
print(' ')

# If there is more than one Tag with the same name, the first element
# with that Tag name is called.
tag_object = soup.h3
print('Tag Object H3:',tag_object)
print(' ')

# Enclosed in the bold attribute b, it helps to use the tree representation.
# We can navigate down the tree using the child attribute to get the name.
tag_child = tag_object.b
print('Tag Objects Child (b):',tag_child)

parent_tag = tag_child.parent
print('Tag Childs Parent (h3):',parent_tag) # Which is identical to 'tag_object'

# Following the same logic, 'tag_object' parent is the body element.
parent_object = tag_object.parent
print('Tag Childs Object (body):',parent_object)

# And 'tag_object' sibling is the paragraph element
sibling_1 = tag_object.next_sibling
print('Tag Object Slibing 1:',sibling_1)

# Therefore, 'sibling_2' is the 'header' element which is also a sibling
# of both 'sibling_1' and 'tag_object'.
sibling_2 = sibling_1.next_sibling
print('Tag Object Slibing 2:',sibling_2)

# And so on.
sibling_3 = sibling_2.next_sibling
print('Tag Object Slibing 3:',sibling_3)
print(' ')

# HTML ATTRIBUTES
print('HTML ATTRIBUTES')
print(' ')

print('Tag Child (ID):',tag_child['id'])
print('Tag Child (attrs):',tag_child.attrs)

# Alternative
print('Tag Child (ID):',tag_child.get('id'))

print('Tag Child (string):',tag_child.string) # Python string
print('Tag Child (string type):',type(tag_child.string))
print('Tag Child (string str):',str(tag_child.string)) # Unicode string

# FILTER
print('FILTER')
print(' ')

# Filters allow you to find complex patterns, the simplest filter is a string.

table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, "html.parser")

# The 'find_all()' method looks through a tag’s descendants and retrieves
# all descendants that match your filters. The Method signature
# for 'find_all(name, attrs, recursive, string, limit, **kwargs)'.

table_rows = table_bs.find_all('tr')
print('Table Rows:')
print(table_rows)
print(' ')
print('First Row:',table_rows[0])
print('First Row (type):',type(table_rows[0]))
print('First Rows First Child:',table_rows[0].td)
print(' ')

# If we iterate through the list, each element corresponds to a row in the table:
for i,row in enumerate(table_rows):
    print("Row",i,"is",row)
print(' ')
   
for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)
print(' ')

# If we use a list, we can match against any item in that list.
list_input = table_bs.find_all(name=["tr", "td"])
print('List Find All:')
print(list_input) # Returns every line which contains or is a 'tr' and 'td'.
print(' ')

# Attributes

# If the argument is not recognized it will be turned into a filter
# on the tag’s attributes. For example the 'id' argument, Beautiful Soup
# will filter against each tag’s 'id' attribute. For example, the first
# 'td' elements have a value of 'id' of 'flight', therefore we can filter based
# on that 'id' value.

find_id = table_bs.find_all(id="flight")
print('Find ID equal to Flight:',find_id)

find_string = table_bs.find_all(string="Florida")
print('Find string equal to Florida:',find_string)

list_input = table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print('Find URL equal to input:',list_input)

url_true = table_bs.find_all(href=True)
print('Find any URLs:',url_true)

find_boldest = soup.find_all(id='boldest') # Uses the previous soup object
print('Find boldest:',find_boldest)
print(' ')

# FIND
print('FIND')
print(' ')

two_tables = "<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
two_tables_bs = BeautifulSoup(two_tables,'html.parser')

find_table = two_tables_bs.find("table")
print('Find Table:',find_table)
print('Find Table and Pizza:',two_tables_bs.find("table",class_='pizza'))

# Downloading And Scraping The Contents Of A Web Page
url = "http://www.ibm.com"
data  = requests.get(url).text
soup = BeautifulSoup(data,'html.parser')

for link in soup.find_all('a',href=True):
    print(link.get('href'))

i = 1
for link in soup.find_all('img'):
    print(i)
    print('Link:')
    print(link)
    print('Link (src):')
    print(link.get('src'))
    i+=1
print(' ')

# Scrape data from HTML tables

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
data = requests.get(url).text
soup = BeautifulSoup(data,'html.parser')

# Find A html table in the web page:
table = soup.find('table') # In HTML table is represented by the tag <table>.

for row in table.find_all('tr'): # In HTML table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # In HTML a column is represented by the tag <td>
    color_name = cols[2].string # Store the value in column 3 as color_name
    color_code = cols[3].string # Store the value in column 4 as color_code
    print("{} ---> {}".format(color_name,color_code))
print(' ')

# Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas

import pandas as pd

url = "https://en.wikipedia.org/wiki/World_population"
data = requests.get(url).text
soup = BeautifulSoup(data,'html.parser')

# Find ALL html tables in the web page:
tables = soup.find_all('table')
print('Number of tables found:',len(tables)) # How many tables were found by checking the length of the tables list.
print(' ')

for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)

# Locate the table name of the table "10 most densely populated countries"
print(tables[table_index].prettify())

# After finding the table, we can search it by its title row:
columns = ["Rank", "Country", "Population", "Area", "Density"]
population_data = pd.DataFrame(columns)
# NOTE: DataFrame will be removed in future versions of pandas.

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

print('Table Found:')
print(population_data) # Not correct?
print(' ')

# Scrape data from HTML tables into a DataFrame using BeautifulSoup and read_html

print('Fifth Table:')
print(pd.read_html(str(tables[5]), flavor='bs4')) # This is an list of 1 element.
print(' ')

population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]
print('Fifth Table First Element:')
print(population_data_read_html) # First element of the previous list.
print(' ')

# Scrape data from HTML tables into a DataFrame using read_html

dataframe_list = pd.read_html(url, flavor='bs4')
print('Number of DataFrames found:',len(dataframe_list))

# Finally, we can pick the DataFrame we need out of the list.
print(dataframe_list[5])

# We can also use the match parameter to select the specific table we want.
print(pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0])
