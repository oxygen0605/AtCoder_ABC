N, Y= map(int, input().split())

flag = False
for j in range(9):
	
	for j in range(N+1-i):
		k = (Y - (10000*i+5000*j))//1000
		if(i + j + k == N):
			flag = True
			print(i, j, k)
			break
	if flag is True:
		break
if flag is False:
	print(-1,-1,-1)

"""
flag = False
for i in range(N+1):
	for j in range(N+1-i):
		k = (Y - (10000*i+5000*j))//1000
		if(i + j + k == N):
			flag = True
			print(i, j, k)
			break
	if flag is True:
		break
if flag is False:
	print(-1,-1,-1)

try:	
	for i in range(N+1):
		zandaka = Y - (10000*i)
		for j in range(N+1-i):
			k = (zandaka - 5000*j)//1000
			if(i + j + k == N):
				print(i, j, k)
				raise Exception
	print(-1,-1,-1)
except Exception:
	pass

flag = False
for i in range(N+1):
	for j in range(N+1-i):
		k = (Y - (10000*i+5000*j))//1000
		if(i + j + k == N):
			flag = True
			print(i, j, k)
			break
	if flag is True:
		break
if flag is False:
	print(-1,-1,-1)
"""
