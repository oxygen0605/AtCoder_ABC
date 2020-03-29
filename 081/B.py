N = int(input())
B = list(map(int, input().split()))
out = 0
flag = 0

while(1):
	for i in range(len(B)):
		if B[i] % 2 != 0:
			flag = 1
			break
		else:
			B[i] /= 2
	if(flag == 1): break
	out += 1
	
print(out)
