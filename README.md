# l1f19bscs0408

LIMIT = 1000000

x=[1] * (LIMIT + 1)
X[0] = x[1] = 0

primes = []
length =0

for i in range(2, LIMIT) :
if x[i]:
primes.append(i)
length += 1

for j in range (i * i, LIMIT + 1, i)
x[j] = 0

s= 0
prev = -1
cnt = -1

for i in range (length) :
s=0

for j in range(i, length):

S += primes[j]

if s> LIMIT:
break

if x[s] and cnt < j - i + 1:
cnt = j - i + 1
prev = s
print (prev)

