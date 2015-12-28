# useful facts
# - all rational numbers are fractions and all fractions are rationals, by
# definition
# - all rationals are either terminating or repeating; proof is algebraic
# solution uses long division algorithm
# q: do all repeating decimals have primes in the denominator? no. for example,
# 23/99
# q: do all repeating decimals have a denominator coprime to 10? yes.
# a decimal number can be represented in base b by writing it as a linear
# combination of all powers of the base, with the weights being < b.
# taking the coefficients of this linear combination, we get the base b
# representation of the decimal number. we shift this representation left so
# that no numbers except 0 are right of the decimal point. let the number of
# places shifted be an integer k, and the result after the shift be a.
# now we have the same number we were trying to represent, which is a rational
# number, as a fraction in its lowest terms, as n/d. by dfn n and d are
# coprime. this representation is = to a/b^k. set them equal, and we get nb^k =
# ad. so if p is a prime factor of d, it must divide b. and if it divides b,
# then a will be an integer, which means the number can be represented in base b
# as a terminating decimal (otherwise a will be decimal no matter how large k
# is, meaning no matter how much we shift there will still be decimals left
# over). this is trivially true for d when d consists of only prime divisors of
# b, 
# but what if we contain other divisors in d? no.
# note: we assume any number can be represented in base b. we can use an
# algorithm to do this conversion. as for uniqueness, consider the
# representation of a pint. and another representation that is different but of
# the same value. their difference (which is 0) will suggest that the coefficients must be
# equal, meaning they have to be the same.

# in retrospect all this was irrelevant bc we are using long division


# keep track of resulting remainders and if remainders repeat then we have
# repetition because the behavior for a remainder will be the same if the
# remainder is the same (because the digits added will always be 0).
def recurring_cycle_length(d)
  digits = []
  r_digits = []
  numerator = 1 # we are computing 1/d
  while true
    r = numerator % d
    if (r_digits.include? r)
      return r_digits.length - r_digits.index(r)
      break
    end
    r_digits.push(r)
    numerator = r
    numerator *= 10 # adding next digit, a 0
    digits.push(numerator/d)
  end
end

d = 2
m = 0
while (d < 1000)
  t = recurring_cycle_length(d)
  if (t > m)
    m = d
  end
  d += 1
end
puts "sol: #{m}"
