import requests

target = 'http://stanleymemer-env.us-east-1.elasticbeanstalk.com'
target = 'http://localhost:5000'

data = {'url':'https://scontent.fphl2-1.fna.fbcdn.net/v/t1.0-9/16142187_1307198629351081_6902234315396804235_n.jpg?oh=5da5685f0cfc5288d6fc99759faf17eb&oe=59476D9A'}
result = requests.post(target+'/api/check_image', json = data)
print(result.json())
