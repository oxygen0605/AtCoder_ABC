N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum=0

for i in range(0, N):
	if (A[i] >= B[i]): sum += B[i]
	else:
		if(A[i+1] >= B[i]-A[i]):
			sum += B[i]
			A[i+1] = A[i+1] - (B[i]-A[i])
		else:
			sum += A[i]+A[i+1]
			A[i+1] = 0

print(sum)
