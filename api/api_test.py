import requests

target = 'http://stanleymemer-env.us-east-1.elasticbeanstalk.com'
target = 'http://localhost:5000'


urls = [
		'https://i.ytimg.com/vi/tYBk4kLHPkk/maxresdefault.jpg',
		'https://scontent.fphl2-1.fna.fbcdn.net/v/t1.0-9/16142187_1307198629351081_6902234315396804235_n.jpg?oh=5da5685f0cfc5288d6fc99759faf17eb&oe=59476D9A',
		'https://s-media-cache-ak0.pinimg.com/736x/16/ed/16/16ed164f84a3ccf15964a493ccd81f38.jpg'
	]


data = {'url':urls[3]}
result = requests.post(target+'/api/check_image', json = data)
print(result.json())
