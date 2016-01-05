# observe that for n^2+an+b to yield a prime at n=0, b must be prime. also
# observe that when n=1, for 1+a+b to be a prime, a must be odd. this is because
# all primes greater than 2 are odd. and since b will be odd, a must also be odd
# to make the resulting number odd.

# why does x*x optimization work? because all multiples of x from 1x to x-1 x
# will be covered by previous iterations
def sieve(n)
  # create array from 1 to n
  primes = Array.new(n+1){ true }
  bound = Math.sqrt(n).ceil # set bound, which is sqrt(n)
  (2..bound).each do |x|
    if primes[x]
      c = 0
      while (i = (x*x+(c*x))) <= n # uses optimization of x*x
        primes[i] = false
        c += 1
      end
    end
  end
  return primes
end

def is_prime local_arg
  Proc.new do |x|
    local_arg[x]    
  end
end
$m = 1000
$is_prime = is_prime sieve($m)

# num of primes for consecutive values of n beginning with n = 0 for n^2+an+b
def num_primes(a, b)
  if (b > $m)
    $m *= 2
    $is_prime = is_prime sieve($m)
  end
  if $is_prime.call(b)
    if a.odd?
      n = 0
      while true
        c = n*n+(a*n)+b
        if c > $m
          $m *= 2
          $is_prime = is_prime sieve($m)
        end
        if !$is_prime.call(c)
          return n
        end
        n+=1
      end
    else
      return 1
    end
  else
    return 0
  end
end
# count = 1
# sieve(10000000).each_with_index{ |x,i|
#   if x
#     puts "#{i} #{count}"
#     count += 1
#   end
# }

h = 0
hp = 0
(-999..999).each do |a|
  (-999..999).each do |b|
    tmp = num_primes(a,b)
    if tmp > h
      h = tmp
      hp = a*b
    end
  end
end

puts h, hp

