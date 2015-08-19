import math

# naive factorial and sum of digits is trivial, so just use builtin functions instead.

fact_res = math.factorial(100)
answer = sum(map(int, str(fact_res)))
print answer
