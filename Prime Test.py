def sieve (limit):
    def sieveHelper ( x ):
        return not [y for y in range(2,x) if x % y == 0]
    return [x for x in range(2,limit) if sieveHelper(x)]

#True = 'inconclusive', False = 'composite'
def millersTest (n, b):
    def step1 (n, b):
        k = 0
        while ((n - 1) / pow(2,k)) == ((n - 1) // pow(2,k)):
            k += 1
            if ((n - 1) / pow(2,k)) != ((n - 1) // pow(2,k)):
                k -= 1
                break
        q = (n - 1) // pow (2,k)
        return step2(n, b, 0, pow(b,q,n), k)
    def step2 (n, b, i, r, k):
        if (i == 0 and r == 1) or (i >= 0 and r == (n-1)):
            return True
        return step3(n, b, i+1, pow(r,2,n), k)
    def step3 (n, b, i, r, k):
        if (i < k):
            return step2 (n, b, i, r, k)
        return False
    if n % 2 == 0:
        return False
    return step1 (n, b)

#Will only find factors up to the highest in primeList
def factors (n, factorSet, primeList):
    for x in primeList:
        if n % x == 0:
            factorSet.add(x)
            return factors((n // x), factorSet, primeList)
    if n != 1:
        factorSet.add(n)
    return factorSet

#Primality test as defined by Coutinho, ISBN 1-561881-082, Ch. 10 S. 2, p.154
#True = 'prime', False = 'composite'
def primeTest (n, primeList):
    factorSet = factors(n-1, set(), primeList)
    for x in factorSet:
        exist = False
        for y in range(2,(n-1)):
            if (pow(y,n-1,n) == 1) and not (pow(y, (n-1)//x, n) == 1):
                exist = True
                break
        if not exist:
            return False
    return True

#Primality test taken from same text as above, p.155
#True = 'prime', False = 'composite'
def primeTestFinal (n, pL = sieve(5000)):
    if n in pL:
        return True
    for x in pL:
        if n % x == 0:
            return False
    for x in range(0,20):
        if not millersTest(n,pL[x]):
            return False
    return primeTest(n, pL)
