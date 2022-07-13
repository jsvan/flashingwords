import time

with open("./texts/streetcar1.txt") as F:
	f = [x.split('\n') for x in F.read().split('\n\n\n')[0].split('\n\n')]

for i in f:
	for _ in range(10):
		for j in i:
			print(' ', j, '                  ',end='\r')
			time.sleep(0.1)
	print('                        ')




with open("./texts/questions1.txt") as F: 
	f = F.read().split('\n\n')

with open('./texts/answers.txt') as F:
	q = [x.split('\n')[0] for x in F.read().split('\n\n')]

for i, ff in enumerate(f):
	print(ff)
	input()
	print(q[i])
	time.sleep(1)
	print('\n')