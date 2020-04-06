from fractions import gcd
A, B, C, D = map(int, input().split())

ca = (A-1)//C 
cb = B//C

da = (A-1)//D
db = B//D

lcm = C * D //gcd(C,D)
cda = (A-1)//lcm
cdb = B//lcm

print(B-A+1-((cb-ca)+(db-da)-(cdb-cda)))
