import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import matplotlib.patches as patches
from PIL import Image
import os
import csv
import numpy as np
import pandas as pd

filename = "training.csv"
fields = []
rows = []
dic = {}
with open(filename, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	fields = next(csvreader)
	temp = 0
	for i in csvreader:
		rows.append(i)
		#print(i[0])
		dic[i[0]] = temp
		temp = temp+1

data = pd.DataFrame()
rows = np.array(rows)
# as the images are in train_images folder, add train_images before the image name
#stt = input("enter the name of the folder where you saved the images")
listt = os.listdir('./training_images')
print(listt)
data['format'] = listt

for i in range(data.shape[0]):
    data['format'][i] = 'training_images/' + data['format'][i]


# add xmin, ymin, xmax, ymax and class as per the format required'
for i in range(len(listt)):   
    print(dic[listt[i]])
    print(i)
    data['format'][i] = data['format'][i] + ',' + str(rows[dic[listt[i]]][1]) + ',' + str(rows[dic[listt[i]]][3]) + ',' + str(rows[dic[listt[i]]][2]) + ',' + str(rows[dic[listt[i]]][4]) + ',' + 'RBC'

data.to_csv('annotate.txt', header=None, index=None, sep=' ')

