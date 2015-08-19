# max path sum

# data processing
raw_data = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

data = []
for s in raw_data.split('\n'):
    data.append(map(int, s.split()))

# inc for indices for naive brute force
def inc(indices):
    i = len(indices)-1
    while (indices[i]+1-indices[i-1] == 2):
        i -= 1
    val = indices[i]+1
    while (i < len(indices)):
        indices[i] = val
        i += 1
    return not (indices[0] > 0)
          
# naive brute force
def naive_sol(data):
    indices = [0] * len(data)
    m = 0
    Unfinished = True
    while (Unfinished):
        tmp = 0
        for i in range(0, len(data)):
            tmp += data[i][indices[i]]
        m = max(m, tmp)
        Unfinished = inc(indices)
    print m
    
naive_sol(data)

# heuristic that doesn't work
#  def test(data):
#     m = 0
#     for l in data:
#         m += max(l)
#     return m

# related problem: how many different routes are there? 2^(number of rows)
# because each row doubles the number of routes, as each item in each row can
# map to 2 numbers of the next row
