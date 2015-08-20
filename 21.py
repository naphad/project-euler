from math import floor, sqrt

def is_prime(n):
    d = {}
    u = floor(sqrt(n))
    i = 2
    # trial division: works pretty well for testing 600 billion
    while (i <= u):
        if (n % i == 0):
            return False
        i += 1
    return True
    
def get_prime_factors(n):
    p = []
    u = floor(sqrt(n))
    i = 2
    if (is_prime(n)):
        return [n]
    while (i <= u):
        while (n % i == 0):
            n /= i
            p.append(i)
        if (n == 1):
            return p
        if (is_prime(n)):
            p.append(n)
            return p
        else:
            i += 1
    return p

print get_prime_factors(200)
            
def get_proper_divisors(n):
    divisors = [1]
    if (n == 1):
        return [0] # edge
    for i in xrange(2, int(floor(n**.5))):
        if (n % i == 0):
            divisors.append(i)
            divisors.append(n/i)
    if (n % (n**.5) == 0):
        divisors.append(int(n**.5))
    return divisors

def naive_cache_sol(n):
    amicables = {}
    total = []
    for i in xrange(2, n):
        if (i in amicables):
            continue
        d = get_proper_divisors(i)
        s = sum(d)
        if (i >= s): # optimization: has already been checked if >, if = then invalid
            continue
        s2 = sum(get_proper_divisors(s))
        if (i == s2):
            total.append(i)
            if (s < n):
                total.append(s)
        if (s > i):
            amicables[s] = True
        
    return sum(total)

def naive_sol(n):
    total = []
    for i in xrange(2, n):
        d = get_proper_divisors(i)
        s = sum(d)
        if (i >= s): # optimization: has already been checked if >, if = then invalid
            continue
        s2 = sum(get_proper_divisors(s))
        if (i == s2):
            total.append(i)
            if (s < n):
                total.append(s)
    return sum(total)

# suppose t(n) is sum of all divisors of N. d(n) is only sum of proper divisors.
# then t(n) = d(n) + n. let p be a prime number. then t(p) = p + 1. also,
# t(p^a) = 1 + p + p^2 + p^3 + ... + p^a because divisors of p^a are all the combinations
# of its factors. multiply t(p^a) by p: p*t(p^a) = p + p^2 + p^3 + p^4 + ... + p^a+1. Subtract
# t(p^a) from p*t(p^a) = (p-1)*t(p^a) = p^a+1 - 1 => t(p^a) = (p^a+1 - 1) / (p-1). So through
# trivial algebra we have a formula for sum of divisors of a prime. we can do better.
# observe that
def better_sol(n):

import time

input_size = 100000

start = time.time()
ans = naive_sol(input_size)
elapsed = time.time() - start
print("%s found in %s seconds with NAIVE solution and input size %s") % (ans,elapsed,input_size)
 
start = time.time()
ans = naive_cache_sol(input_size)
elapsed = time.time() - start
print("%s found in %s seconds with NAIVE CACHE solution and input size %s") % (ans,elapsed,input_size)
