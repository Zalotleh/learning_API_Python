"""
API Documentation
In order to ensure we make a successful request, when we work with APIs it’s important to consult the documentation.
Documentation can seem scary at first, but as you use documentation more and more you’ll find it gets easier.

We’ll be working with the Open Notify API, which gives access to data about the international space station.
It’s a great API for learning because it has a very simple design, and doesn’t require authentication.

Often there will be multiple APIs available on a particular server. Each of these APIs are commonly called endpoints.
The first endpoint we’ll use is http://api.open-notify.org/astros.json, which returns data about astronauts currently
in space.

If you click the link above to look at the documentation for this endpoint, you’ll see that it says This API takes no
inputs. This makes it a simple API for us to get started with. We’ll start by making a GET request to the endpoint
using the requests library:
"""
import requests
import json
from datetime import datetime


response = requests.get("https://api.open-notify.org/astros.json")

print(response.status_code)

""" 
Working with JSON Data in Python
JSON (JavaScript Object Notation) is the language of APIs. JSON is a way to encode data structures that ensures that 
they are easily readable by machines. JSON is the primary format in which data is passed back and forth to APIs,
 and most API servers will send their responses in JSON format.

You might have noticed that the JSON output we received from the API looked like it contained Python dictionaries, 
lists, strings and integers. You can think of JSON as being a combination of these objects represented as strings. 

Python has great JSON support with the json package. The json package is part of the standard library, so we don’t have 
to install anything to use it. We can both convert lists and dictionaries to JSON, and convert strings to lists 
and dictionaries. In the case of our ISS Pass data, it is a dictionary encoded to a string in JSON format.

The json library has two main functions:

json.dumps() — Takes in a Python object, and converts (dumps) it to a string.
json.loads() — Takes a JSON string, and converts (loads) it to a Python object.
The dumps() function is particularly useful as we can use it to print a formatted string which makes it easier 
to understand the JSON output,
"""


def json_print(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


json_print(response.json())

"""
output:

{
    "message": "success",
    "request": {
        "altitude": 100,
        "datetime": 1568062811,
        "latitude": 40.71,
        "longitude": -74.0,
        "passes": 5
    },
    "response": [
        {
            "duration": 395,
            "risetime": 1568082479
        },
        {
            "duration": 640,
            "risetime": 1568088118
        },
        {
            "duration": 614,
            "risetime": 1568093944
        },
        {
            "duration": 555,
            "risetime": 1568099831
        },
        {
            "duration": 595,
            "risetime": 1568105674
        }
    ]
}

"""

"""
using parameters
"""

parameters = {
    "lat": 40.71,
    "lon": -74
}

response = requests.get("https://api.open-notify.org/iss-pass.json", params=parameters)

json_print(response.json())

"""
output

{
    "message": "success",
    "request": {
        "altitude": 100,
        "datetime": 1568062811,
        "latitude": 40.71,
        "longitude": -74.0,
        "passes": 5
    },
    "response": [
        {
            "duration": 395,
            "risetime": 1568082479
        },
        {
            "duration": 640,
            "risetime": 1568088118
        },
        {
            "duration": 614,
            "risetime": 1568093944
        },
        {
            "duration": 555,
            "risetime": 1568099831
        },
        {
            "duration": 595,
            "risetime": 1568105674
        }
    ]
}

"""

pass_times = response.json()['response']
json_print(pass_times)

"""
output:

[
    {
        "duration": 395,
        "risetime": 1568082479
    },
    {
        "duration": 640,
        "risetime": 1568088118
    },
    {
        "duration": 614,
        "risetime": 1568093944
    },
    {
        "duration": 555,
        "risetime": 1568099831
    },
    {
        "duration": 595,
        "risetime": 1568105674
    }
]


"""

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)

"""
output:

[1568082479, 1568088118, 1568093944, 1568099831, 1568105674]

"""


times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)

"""
output:

2019-09-09 21:27:59
2019-09-09 23:01:58
2019-09-10 00:39:04
2019-09-10 02:17:11
2019-09-10 03:54:34
"""


