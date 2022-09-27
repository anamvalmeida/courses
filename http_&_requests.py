"""
    HTTP and Requests

Author: Ana M. Almeida
Date: 27.09.2022

Guide: 
"""

import requests
import os 
from PIL import Image
from IPython.display import IFrame

url = 'https://www.ibm.com/'
r = requests.get(url)
print('Request:',r)
print('Request Status:',r.status_code)

# A request header is an HTTP header that can be used in an HTTP request
# to provide information about the request context, so that the server
# can tailor the response.
# The request-header fields allow the client to pass additional information
# about the request, and about the client itself, to the server.
print('Request Header:',r.request.headers) # User-Agent

print('Request Body:', r.request.body)

# Response headers hold additional information about the response, like its
# location or about the server providing it.
header = r.headers # This returns a python dictionary of HTTP response headers.
print('Header:',header) # Server

print('Date:',header['date'])
print('Type of Data:',header['Content-Type'])

print('Encoding:',r.encoding)
print('First 100 characters:',r.text[0:100])
print(' ')

# LOAD IMAGES (non-text requests)
print('LOAD IMAGES (non-text requests)')
url = 'https://upload.wikimedia.org/wikipedia/en/0/00/IBM_Watson_Logo_2017.png'
r = requests.get(url)
print('Request Header:',r.headers)
print('Request Header (content-type):',r.headers['Content-Type'])
print(' ')

# Saving the image
path = os.path.join(os.getcwd(),'image.png') # getcwd() returns current working
# directory of a process

with open(path,'wb') as f:
    f.write(r.content)
Image.open(path)

# QUESTION 1: WRITE 'wget'
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path = os.path.join(os.getcwd(),'example1.txt')
r = requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)

# GET REQUEST WITH URL PARAMETERS
print('GET REQUEST WITH URL PARAMETERS')
url_get='http://httpbin.org/get'
# Base URL: httpbin.org
# Route: /get

# A query string is a part of a uniform resource locator (URL), this sends other
# information to the web server. The start of the query is a ?, followed by a
# series of parameter and value pairs. The first parameter name is name and the
# second parameter name is ID.
payload={"name":"Joseph","ID":"123"}


# Then passing the dictionary payload to the params parameter of the  get() function:
r = requests.get(url_get,params = payload)
print('URL:',r.url)
print('Request Body:', r.request.body)
print('Request Status:',r.status_code)
print('Text:',r.text)
print('Request Header (content-type):',r.headers['Content-Type'])
# As the content 'Content-Type' is in the JSON format we can use the method json(),
# it returns a Python dict:
print('JSON to Python:',r.json) #  It is often used for serializing structured data and
# exchanging it over a network, typically between a server and web applications.
print('Arguments:',r.json()['args'])

# POST REQUEST
# Like a GET request, a POST is used to send data to a server, but the POST
# request sends the data in a request body.
url_post='http://httpbin.org/post' # This endpoint will expect data as a file or as a form.

r_post = requests.post(url_post,data = payload)
print("POST request URL:",r_post.url) # It separes the URL from the body.
print("GET request URL:",r.url) # Puts together the URL and the body as one.
print(' ')

print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body) # Thefore, the URL does not present a body (None).
print(' ')

print('JSON to Python:',r_post.json())
print('JSON to Python (form):',r_post.json()['form']) # In this case, it returns the arguments of the body.
