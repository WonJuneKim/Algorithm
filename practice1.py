import sys

read = lambda: sys.stdin.readline().rstrip()

dwarf = [int(read()) for _ in range(9)]

total = sum(dwarf)
one = 0
two = 0

for i in range(9):
    for j in range(i+1, 9):
        if total - (dwarf[i] + dwarf[j]) == 100:
            one, two = dwarf[i], dwarf[j]
            break

dwarf.remove(one)
dwarf.remove(two)
dwarf.sort()

for i in dwarf:
    print(i)