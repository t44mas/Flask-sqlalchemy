from requests import get, post, delete

#
# print(get('http://localhost:5000/api/v2/users').json())
# print(get('http://localhost:5000//api/v2/users/2').json())
# print(get('http://localhost:5000//api/v2/users/asd').json())  # должно быть число а не строка
#
# print(delete('http://localhost:5000/api/v2/users/3').json())
# print(delete('http://localhost:5000/api/v2/users/99').json())  # нет пользователя с id 99
#
# print(post('http://localhost:5000/api/v2/users',
#            json={'name': 'John',
#                  'surname': 'Andreson',
#                  'age': 29,
#                  'position': 'manager',
#                  'speciality': 'mechanic',
#                  'address': '1_module',
#                  'email': 'john@gmail.com'}).json())
# print(post('http://localhost:5000/api/v2/users',
#            json={'name': 'John',
#                  'surname': 'Andreson',
#                  'age': '29',  # должно быть число а не строка
#                  'position': 'manager',
#                  'speciality': 'mechanic',
#                  'address': '1_module',
#                  'email': 'john@gmail.com'}).json())
# print(post('http://localhost:5000/api/v2/users',
#            json={}).json())  # нет данных

print(get('http://localhost:5000/api/v2/jobs').json())
print(get('http://localhost:5000//api/v2/jobs/2').json())
print(get('http://localhost:5000//api/v2/users/asd').json())  # должно быть число а не строка

print(delete('http://localhost:5000/api/v2/jobs/3').json())
print(delete('http://localhost:5000/api/v2/jobs/99').json())  # нет работы с id 99

print(post('http://localhost:5000/api/v2/jobs',
           json={'team_leader': 2,
                 'job': 'clean',
                 'work_size': 120,
                 'collaborators': '1,2,3',
                 'address': '1_module',
                 'is_finished': True}).json())
print(post('http://localhost:5000/api/v2/jobs',
           json={'team_leader': '2',  # должно быть число а не строка
                 'job': 'clean',
                 'work_size': 120,
                 'collaborators': '1,2,3',
                 'address': '1_module',
                 'is_finished': True}).json())
print(post('http://localhost:5000/api/v2/jobs',
           json={}).json())  # нет данных
