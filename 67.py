# max path sum II

# data processing
with open("data/67/triangle.txt", "r") as f:
        raw_data = f.read()

data = []
for s in raw_data.split('\n'):
        data.append(map(int, s.split()))

data = data[:-1] # edge case


