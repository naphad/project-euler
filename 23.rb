#!/usr/bin/ruby

require_relative('lib.rb') # requires relative to current file dir
require 'prime'
require 'set'

UPPER_LIMIT = 20161 # 28123 # deduced by analysis # 20161 was stated on Wolfram
# and brings it down to 2.8s
RANGE = (1..UPPER_LIMIT).to_a

# see 21.py for expl
def divisors(p, a) # p is prime, a is its occurence
  (p**(a+1)-1)/(p-1)
end

def proper_divisors(n)
  s = 1
  n.prime_division.each{|p,a| s *= divisors(p,a)}
  s -= n  
end

def abundant?(n)
  proper_divisors(n) > n
end

# ~5.5 seconds
def naive_sol()
  s = 0
  abundants = RANGE.select{|x| abundant? x}
  tabundants = []
  abundants.each_with_index do |a,i|
    abundants.drop(i).each{|b| tabundants << (a+b) }
  end
#  tmp = RANGE.select{|x| tabundants.include? x} # this is too slow, use -
#  instead
#  for i in tabundants.to_set # to_set takes too long
#    RANGE[i-1] = 0
#  end
  tmp = RANGE - tabundants
  tmp.reduce(:+)

end

ans = 0
tdelta = time { ans = naive_sol() } 
puts "#{ans} took #{tdelta} ms"
