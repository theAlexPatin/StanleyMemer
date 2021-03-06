from flask import jsonify, request, Flask 
from sklearn.externals import joblib
import urllib
import os
from PIL import Image
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from OpenSSL import SSL

knn = joblib.load('knn.pkl')
pca = joblib.load('pca.pkl')
STANDARD_SIZE = (300, 167)

application = Flask(__name__)


@application.route('/api/check_image', methods=['GET'])
def check_image():
	try:
		imgUrl = request.json['url']
		#imgUrl = "https://i.ytimg.com/vi/tYBk4kLHPkk/maxresdefault.jpg"
		path = imgUrl.split('/')[-1]
		urllib.request.urlretrieve(imgUrl, path)
		img = img_to_matrix(path)
		img = pca.transform(img)
		prediction = knn.predict(img)

		if prediction == 1:
			os.remove(path)
			print('meme')
			return jsonify({'type':'meme', 'src':imgUrl})
		else:
			os.remove(path)
			print('image')
			return jsonify({'type':'image'})
	except:
		try:
			os.remove(path)
		except:
			pass
		print('error')
		return jsonify({'type':'error'})

def img_to_matrix(filename):
	img = Image.open(filename)
	img = img.resize(STANDARD_SIZE)
	img = np.array(img)
	img = img.flatten()
	return img

if __name__ == '__main__':
	#context= ('host.cert', 'host.key')
	#application.run(debug=True, ssl_context=context)
	application.run(debug=True)