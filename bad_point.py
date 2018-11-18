#coding:utf-8
# 统计一些异常的数据 string_data=[] status: true/false
import re

empty_true = []
empty_false = []

empty_ua=[]

# 总数
count = 0

success=0
failed=0

for line in open('data_samples.txt'):

	if line.startswith('(['):
		count += 1

		pieces=line.strip().split(',',3)

		if line.startswith('([],'):

			empty_ua.append(pieces[3])

			# print(line)

			if 'true' in line:

				empty_true.append([pieces[2],pieces[3]])
			if 'false' in line:
				empty_false.append([pieces[2],pieces[3]])

	if 'true' in line: 
		success+=1
	if 'false' in line:
		failed+=1

print(count,success,failed)

print(len(empty_true),len(empty_true)/count)

for item in empty_true:
	print(item)

print(len(empty_false),len(empty_false)/count)
for item in empty_false:
	print(item)

print(len(empty_ua),len(set(empty_ua)))

empty_ua_dict={}
for item in empty_ua:
	empty_ua_dict[item]=empty_ua_dict.get(item,0)+1

for item in sorted(empty_ua_dict.items(),key = lambda x:x[1],reverse = True):
	print(item)


empty_true_ip = []
for item in empty_true:
	if item[0] not in empty_true_ip:
		empty_true_ip.append(item[0])

print(empty_true_ip)



