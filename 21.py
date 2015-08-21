# -*- coding: utf-8 -*- # needed b/c of math symbols
from math import floor, sqrt

def get_sieve(n):
#    n *= 3
    sieve = [True]*n # initialize to all trues
#    sieve = {}
#    for i in xrange(2, n):
#        sieve[i] = True
        
    u = int(floor(sqrt(n)))
    for i in xrange(2, u+1):
        if (not sieve[i]):
            continue
        tmp = i+i
        while (tmp < n):
            sieve[tmp] = False
            tmp += i
    return sieve

input_size = 10000

sieve = get_sieve(input_size)

def is_prime(n):
    return sieve[n]
#     d = {}
#     u = floor(sqrt(n))
#     i = 2
#     # trial division: works pretty well for testing 600 billion
#     while (i <= u):
#         if (n % i == 0):
#             return False
#         i += 1
#     return True

# prime factorization
def get_prime_factors(n):
    p = []
    u = floor(sqrt(n))
    i = 2
    if (is_prime(n)):
        return [(n, 1)]
    while (i <= u):
        a = 0
        tmp = False
        while (n % i == 0):
            tmp = True
            n /= i
            a += 1
        if (tmp):
            p.append((i, a))
        if (n == 1):
            return p
        if (is_prime(n)):
            p.append((n, 1))
            return p
        else:
            i += 1
    return p

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

# suppose t(n) is sum of all divisors of N. d(n) is only sum of proper
# divisors.  then t(n) = d(n) + n. let p be a prime number. then t(p)
# = p + 1. also, t(p^a) = 1 + p + p^2 + p^3 + ... + p^a because
# divisors of p^a are all the combinations of its factors. multiply
# t(p^a) by p: p*t(p^a) = p + p^2 + p^3 + p^4 + ... + p^a+1. Subtract
# t(p^a) from p*t(p^a) = (p-1)*t(p^a) = p^a+1 - 1 => t(p^a) = (p^a+1 -
# 1) / (p-1). So through trivial algebra we have a formula for sum of
# divisors of a number that is multiple of a prime. to generalize for
# all numbers, we need to prove that t(n) is multiplicative
# (f(ab)=f(a)f(b)) for two coprimes, because two primes are always
# coprime to each other. then we can apply the formula to the number's
# prime factorization. the proof is trivial: t(ab) = sum of all divisors d
# s.t. d|ab. because a and b are coprime, each divisor d must be a product
# of two unique coprimes d1 and d2, which divide a and b, respectively.
# this equates to a double summation (which are tantamount to double fors):
# t(ab) = ∑d1|a ∑d2|b (d1d2). This is because the sum of all the divisors for
# t(ab) is the sum of all the combination of all the divsors of a and b.
# the equation then simplifies to: t(ab) = d11(d21+...+d2n)+...+d1n(d21+...+d2n)
# = (∑d1|a d1)(∑d2|b d2). Hence the formula to compute the sum of
# divisors for any number through prime factorization is t(n)=∏p|n(p^(a+1)-1/p-1)
# where p is a unique prime divisor of n and a is the number of times it occurs.

# sums all divisors of a prime or multiple of prime; a is how many times the prime occurs
def sum_divisors_prime(p, a):
    if (a == 1):
        return p+1
    return (p**(a+1)-1)/(p-1)

def sum_proper_divisors(n):
    prime_factors = get_prime_factors(n)
    s = 1
    for (p, a) in prime_factors:
        s *= sum_divisors_prime(p, a)
    return s - n

def better_sol(n):
    amicables = {}
    total = 0
    for i in xrange(2, n):
        if (i in amicables):
            continue
        s = sum_proper_divisors(i)
        if (i >= s):
            continue
        else:
            if (s >= n): # our implementation assumes s >= n are invalid pairs... if we assume otherwise then we have to estimate a bound for the sieve.
                continue
            s2 = sum_proper_divisors(s)
            if (s2 == i):
                total += i
                if (s < n):
                    total += s
            amicables[s] = True
    return total

import time

start = time.time()
ans = naive_sol(input_size)
elapsed = time.time() - start
print("%s found in %s seconds with NAIVE solution and input size %s") % (ans,elapsed,input_size)
 
start = time.time()
ans = naive_cache_sol(input_size)
elapsed = time.time() - start
print("%s found in %s seconds with NAIVE CACHE solution and input size %s") % (ans,elapsed,input_size)

start = time.time()
ans = better_sol(input_size)
elapsed = time.time() - start
print("%s found in %s seconds with BETTER solution and input size %s") % (ans,elapsed,input_size) # this solution is better only if we use a sieve for is_prime()... better_sol() about 2x faster on my machine
