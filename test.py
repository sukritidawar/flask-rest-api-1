import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10000, "name": "Sukriti Intro", "views": 1000000},
        {"likes": 1000, "name": "How to make REST API", "views": 10000},
        {"likes": 100, "name": "Hello", "views": 500}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


input()
response = requests.get(BASE + "video/2")
print(response.json())

input()
response = requests.patch(BASE + "video/2", {"views": 99})
print(response.json())

input()
response = requests.delete(BASE + "video/2")
print(response)

input()
response = requests.get(BASE + "video/2")
print(response.json())