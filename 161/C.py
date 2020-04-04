N, K = map(int, input().split())
amari = N%K
print(min(amari,abs(amari-K)))
