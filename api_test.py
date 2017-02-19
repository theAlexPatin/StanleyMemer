import requests

data = {'url':'https://i.ytimg.com/vi/tYBk4kLHPkk/maxresdefault.jpg'}
result = requests.post('http://localhost:5000/api/check_image', json = data)
print(result.json())
