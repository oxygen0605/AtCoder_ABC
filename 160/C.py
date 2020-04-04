K, N = map(int, input().split())
A =  list(map(int, input().split()))

mini = K
right = left = K
for i in range(N):
	l_begin = i-1
	r_begin = i+1
	if i == 0:
		l_begin = N-1
		right = A[l_begin] - A[i]
		left = K - (A[r_begin]-A[i])
	elif i == N-1:
		r_begin = 0
		right = K - (A[i]-A[l_begin])
		left = A[i] - A[r_begin]
	else:
		right = K - (A[i]-A[l_begin])
		left = K - (A[r_begin]-A[i])
	local = min(right, left)
	if local < mini:
		mini = local

print(mini)
