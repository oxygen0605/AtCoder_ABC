N, K, Q = map(int, input().split())
A = [int(input()) for i in range(Q)]
score = [0 for i in range(N)]
for a in A:
	score[a-1] += 1
# ���������`�F�b�N 
for i in range(N):
	if K-Q+score[i] > 0:
		print("Yes")
	else:
		print("No")
