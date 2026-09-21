# A GET request is an HTTP request normally used to retrieve
# information or data from a server.
#
# A POST request is an HTTP request normally used to send data
# to a server for processing or for creating a new resource.
#
# The main difference is that GET is primarily used for
# retrieving data, while POST is primarily used for sending
# data to the server.
#
# The Python requests library provides functions such as
# requests.get() and requests.post() for communicating with
# web APIs.
#
# Data can be sent with a POST request using the json parameter
# when the API expects JSON data.

import requests


# Example API URL
url = "https://httpbin.org/post"

# Data that will be sent to the API
data = {
    "name": "Tinotenda",
    "age": 25,
    "course": "Information Technology"
}

# Send the POST request with the data as JSON
response = requests.post(url, json=data)

# Display the HTTP status code returned by the server
print("Status Code:", response.status_code)

# Display the response received from the API
print("Response:")
print(response.json())