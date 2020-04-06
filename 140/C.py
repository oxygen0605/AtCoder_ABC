N = int(input())
B = list(map(int, input().split()))
sum = B[0]
for i in range(1, N-1):
	sum += min(B[i],B[i-1])
sum += B[N-2]
print(sum)
