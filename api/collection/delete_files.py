import sys
import os

for file in os.listdir('images/'):
	if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
		pass
	else:
		os.remove("images/" + file)
for file in os.listdir('memes/'):
	if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
		pass
	else:
		os.remove("memes/"+file)