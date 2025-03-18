from requests import get, post, delete

# print(get('http://localhost:5000/api/jobs').json())
# print(get('http://localhost:5000/api/jobs/1').json())
# print(get('http://localhost:5000/api/jobs/99').json())
# print(get('http://localhost:5000/api/jobs/pioep').json())

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1,
                 'job': 'уборка',
                 'work_size': 2,
                 'collaborators': '1, 2',
                 'is_finished': True}).json())

print(post('http://localhost:5000/api/jobs', json={}).json())  # некоректный запрос: пустой запрос

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1}).json())  # некоректный запрос: нет необходимых данных

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 'Alan Wake',  # некоректный запрос: 'team_leader' должен быть числом
                 'job': 'уборка',
                 'work_size': 2,
                 'collaborators': '1, 2',
                 'is_finished': True}).json())
