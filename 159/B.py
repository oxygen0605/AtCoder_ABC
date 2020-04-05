S = input()

left = 0
left_end = (len(S)-1)//2 -1
right = len(S)-1
right_start = (len(S)+3)//2 -1
flag = 0

for i in range((len(S)-1)//2):
	if(S[left] != S[right]) or (S[left] != S[left_end]) or (S[right_start] != S[right]):
		flag += 1
		break
	left += 1
	left_end -= 1
	right_start += 1
	right -= 1

if flag == 0:
	print("Yes")
else:
	print("No")
