N = int(input())
A = list(map(int, input().split()))

Alice = 0
Bob = 0
A.sort(reverse=True)
for i, a in enumerate(A):
	if i%2 == 0: Alice += a
	else : Bob += a

print(Alice-Bob)
