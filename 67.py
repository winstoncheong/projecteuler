from pprint import pprint
f = open('./resources/p067_triangle.txt')
vals = []
for line in f.readlines():
    vals.append(list(map(int, line.split())))

def combine_last_rows(vals):
    """Combine last rows, taking the max route"""

    second_last = vals[-2]
    last = vals[-1]
    combined = []

    for i, val in enumerate(second_last):
        combined.append(val + max(last[i], last[i+1]))

    newvals = vals[:-2]
    newvals.append(combined)
    return newvals

while len(vals) > 1:
    vals = combine_last_rows(vals)

print(vals)