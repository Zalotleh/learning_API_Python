import requests

'''There are many different types of requests. The most commonly used one, a GET request, is used to retrieve data. 
Because we’ll just be working with retrieving data, our focus will be on making ‘get’ requests. 

When we make a request, the response from the API comes with a response code which tells us whether our request was 
successful. Response codes are important because they immediately tell us if something went wrong. 

To make a ‘GET’ request, we’ll use the requests.get() function, which requires one argument — the URL we want to make 
the request to. We’ll start by making a request to an API endpoint that doesn’t exist, so we can see what that 
response code looks like. '''

response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")

'''
The get() function returns a response object. We can use the response.status_code attribute to receive the status code 
for our request:
'''

print(response.status_code)


'''
API Status Codes

Status codes are returned with every request that is made to a web server. Status codes indicate information about what 
happened with a request. Here are some codes that are relevant to GET requests:

200: Everything went okay, and the result has been returned (if any).
301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an 
endpoint name is changed.
400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other 
things.
401: The server thinks you’re not authenticated. Many APIs require login credentials, so this happens when you don’t 
send the right credentials to access an API.
403: The resource you’re trying to access is forbidden: you don’t have the right per lessons to see it.
404: The resource you tried to access wasn’t found on the server.
503: The server is not ready to handle the request.
'''

