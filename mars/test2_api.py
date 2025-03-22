from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000//api/v2/users/2').json())
print(get('http://localhost:5000//api/v2/users/asd').json())