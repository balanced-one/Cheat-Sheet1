def primes(n):
    ps=[1]*n
    ps[0]=0; ps[1]=0
    for i, p_i in enumerate(ps[:int(n**0.5)]):
        if p_i:
            for j in range(i+i, n, i):
                ps[j]=0
    return[i for (i, p_i)in enumerate(ps) if p_i]
print(primes(100000000))