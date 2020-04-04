N, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
count = 0

for a in A:
	if a < (total / (4*M)):
		continue
	count += 1

if count >= M:
	print("Yes")
else:
	print("No")
	