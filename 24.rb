#!/usr/bin/ruby

# 0123456789
# 0123456798
# 0123456879
# 0123456897
# 0123456978
# 0123456987
# 0123457689
# 0123457869
# 0123457896
# 0123457968
# 0123457986

# naive solution is to generate all permutations, sort them, and select the
# millionth one. how to generate permutation?
# is there a way to generate permutations in order?

# observe that 9! < 10^6 so solution cannot have a 0 in front. 9! * 3 > 10^6 and
# 9! * 2 < 10^6 so the solution must have a 2 in front. 10^6 - (9! * 2) =
# 274240. So answer is the 274239th number after the first lexicographical
# number beginning with 2 (2013456789). We can continue this process
# indefinitely to reach the answer.

# returns the largest factorial less than n.
def find_fact_bound(n)
  (2...n).each do |x|
    f = (1..x).reduce(:*)
    if f > n
      return f/x # sequence does not go to last elm
    end
  end
end

# finds the largest multiple of factorial of F that can be less than n.
def find_mult_fact_bound(n, f)
  i = 1 
  while ((i*f) < n)
    i += 1
  end
  i-1
end

# runs in O(x^2) time where x is the length of the permutation.
# arg N is the permutation number we are looking for. since this is mil, default
# is 1mil.
# arg ARR is an ORDERED list of valid permutation characters
def mil_permutation(n=1000000, arr)
  f = (1..(arr.length-1)).reduce(:*)
  if f == nil
    return arr[0].to_s # base
  else
    #f = find_fact_bound(n) # find_fact_bound doesnt need to be used b/c we go
    # down consecutively
    m = find_mult_fact_bound(n, f)
    n -= m*f
    d = arr.delete_at(m)
    return d.to_s << mil_permutation(n, arr)
  end
end

arr = *(0..9)
ans = mil_permutation(1000000, arr)
puts ans

