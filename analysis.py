#coding:utf-8
import re
import numpy as np

# 读取数据
def readData(filename):
	track_list=[]
	for line in open(filename):
		# 筛选data!=[] 且验证成功的数据
		if line.startswith('([{') and 'true' in line:
			line=line.strip()
			# for item in re.findall(r"\"x\":(.*?)\,\"y\":(.*?)\}",line.strip()):
			ilist=[]
			for item in re.findall(r'date\":(.*?)\,\"x\":(.*?)\,\"y\":(.*?)\}',line):
				# x,y 坐标
				date,x,y=item[0],item[1],item[2]

				ilist.append([date,x,y])

			pieces=line.split('true,')
			ip_ua=pieces[1].split(',',1)

			track_list.append([ilist,ip_ua[0],ip_ua[1]])
	return track_list

# 轨迹长度分析
def length_analysis(track_list):

	length_arr=np.array(map(lambda x:len(x[0]),track_list))
	print(length_arr.shape)
	print(length_arr.max(),length_arr.min())
	print(sorted(length_arr,key=lambda x:x,reverse=True)[0])

	for item in track_list:
		if len(item[0])<10:
			print(len(item[0]),item)
	


def main():
	# 读数据
	track_list=readData('data_samples.txt')
	print(len(track_list))
	print(track_list[0])

	# 轨迹长度分析
	length_analysis(track_list)
if __name__ == '__main__':
	main()