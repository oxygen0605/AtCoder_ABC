S = input()
T = ''
S = S[::-1]
words = ["dream","dreamer","erase","eraser"]
rev_words = [w[::-1] for w in words]

flag = False
i=0
while(1):
	for w in rev_words:
		s = S[i:i+len(w)]
		if s == w:
			flag = True
			T += w
			i += len(w)
			break
	if T == S:
		ans = "YES"
		break
	if flag == False:
		ans = 'NO'
		break
	flag = False

print(ans)
