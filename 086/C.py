
N = int(input()) 
P = [list(map(int, input().split())) for i in range(N)] 
P.insert(0,[0,0,0])

ans = "Yes"
for i in range(N):
	norm = abs(P[i+1][1]-P[i][1])+abs(P[i+1][2]-P[i][2])
	move = (P[i+1][0]-P[i][0]) - norm
	if ((move%2 != 0) or (move < 0)):
		ans = "No"
		break
	
print(ans)


