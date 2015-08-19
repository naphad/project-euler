# max path sum II

# data processing
with open("data/67/triangle.txt", "r") as f:
        raw_data = f.read()

data = []
for s in raw_data.split('\n'):
        data.append(map(int, s.split()))

data = data[:-1] # edge case

# for explanation see 18.py
def sol(data):
    i = len(data) - 2
    while (i >= 0):
        for j in range(0, i+1):
            data[i][j] += max(data[i+1][j], data[i+1][j+1])
        i -= 1
    print data[0][0]
sol(data)
