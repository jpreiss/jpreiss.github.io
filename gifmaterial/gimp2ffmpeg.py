import sys

lines = list(sys.stdin)
line = lines[1]
values = []
for s in line.split():
    i = int(s) / 255.0
    if i < 0:
        break
    values.append(i)
assert len(values) % 2 == 0
nums = values[0::2]
denoms = values[1::2]
strs = [f"{n}/{d}" for n, d in zip(nums, denoms)]
sys.stdout.write(" ".join(strs))
