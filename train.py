from PIL import Image
from os import listdir
import numpy as np
import pandas as pd 
from sklearn.decomposition import RandomizedPCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.externals import joblib
import random


STANDARD_SIZE = (300, 167)

def img_to_matrix(filename):
	img = Image.open(filename)
	img = img.resize(STANDARD_SIZE)
	img = np.array(img)
	img = img.flatten()
	return img

def train(data, labels):
	train_x = data[0:len(data)*0.8]
	test_x = data[len(data)*0.8+1:]
	train_y = labels[0:int(len(labels)*0.8)]
	test_y = labels[int(len(labels)*0.8+1):]
	pca = RandomizedPCA(n_components=10)
	train_x = pca.fit_transform(train_x)
	test_x = pca.transform(test_x)

	knn = KNeighborsClassifier()
	knn.fit(train_x, train_y)
	joblib.dump(knn, 'knn.pkl', compress=9)
	joblib.dump(pca, 'pca.pkl', compress=9)
	predictions = knn.predict(test_x)
	return predictions
	
	

def batch_run():
	data = []

	path = 'collection/images/'
	labels = []
	images = []
	files = []
	directory = [path+f for f in listdir(path)]
	for f in directory:
		files.append(f)
		images.append(f)
		labels.append(0) #normal image
	path = 'collection/memes/'
	directory = [path+f for f in listdir(path)]
	for f in directory:
		files.append(f)
		images.append(f)
		labels.append(1) #memes
	success_labels = []
	success_images = []
	success_files = []

	for i in range(0,len(images)):
		try:
			j = random.randint(0,len(images)-1)
			img = img_to_matrix(images[j])
			if(len(img) == 150300):
				data.append(img)
				success_images.append(images[j])
				success_labels.append(labels[j])
				success_files.append(files[j])
				print(images[j])
			else:
				print('error')
		except:
			print('error')
	labels = success_labels
	images = success_images
	files = success_files
	print(files)
	data = np.array(data)
	predictions = train(data, labels)
	correct = 0
	incorrect = 0
	for i in range(0,len(predictions)):
		if predictions[i] == 1:
			print('Meme: ' + files[i])
			if '/memes/' in files[i]:
				correct += 1
		else:
			print('Image: ' + files[i])
			if '/images/' in files[i]:
				correct += 1
	print(str.format("Percent Correct: {0}", correct/len(predictions)))

	
	

if __name__ == '__main__':
	batch_run()