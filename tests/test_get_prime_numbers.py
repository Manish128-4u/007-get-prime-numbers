def enter_int(num):
    primes=[2]
    m=3
    if num<2:
        return 0
    while m<=num:
        for n in primes:
            if m%n==0:
                m+=2
                break
         else:
            primes.append(m)
            m+=2
            print(primes)
            return len(primes)
                    
