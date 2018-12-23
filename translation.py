#  pip install googletrans


import json
from pprint import pprint
from googletrans import Translator

translator = Translator()
with open('captions_val2014.json') as data_file:    
    data = json.load(data_file)

file = open('caption.txt','w')
file1 = open('id.txt','w')
file2 = open('image_idtxt','w')

#pprint(len(data['annotations']))
for i in range(len(data['annotations'])):
	print(i)
	translations = translator.translate(data['annotations'][i]['caption'], dest='hi')		
	file.write(translations.text.encode('utf-8'))
	file.write('\n')
	file1.write(str(data['annotations'][i]['id']))
	file1.write('\n')
	file2.write(str(data['annotations'][i]['image_id']))
	file2.write('\n')	

file.close()
file1.close()
file2.close()
	