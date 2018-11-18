#coding:utf-8
import re
import numpy as np
import matplotlib.pyplot as plt
import time

# ilist=[]

# for line in open('data_samples3.txt'):
# 	s=line.strip().replace(" ","").replace("\n","")
# 	if s.startswith('(['):
# 		ilist.append(s)

# f=open('data_samples.txt','w')
# f.write('\n'.join(ilist))
# f.close()


for line in open('data_samples.txt'):

	x_list = []
	y_list = []


	s=line.strip()

	for item in re.findall(r"\"x\":(.*?)\,\"y\":(.*?)\}",s):

		x = item[0]
		y = item[1]

		y_list.append(y)
		x_list.append(x)

		status = 'false'

		if 'true' in s:
			status = 'true'

		print(x,y)


	fig,ax = plt.subplots()
	# ax.scatter(x_list,y_list,c='r',s=10)
	ax.plot(x_list,y_list,c='r')
	plt.title(status)



	for i,txt in enumerate(np.arange(len(x_list))):
		ax.annotate(txt,(x_list[i],y_list[i]))

	plt.show()

	# plt.pause(0)