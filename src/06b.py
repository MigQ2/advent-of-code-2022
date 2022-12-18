

with open("data/06.txt", "r") as f:
    lines = f.read().splitlines() 

l = lines[0]
# for l in lines:

for i in range(14, len(l)):
    letters = l[i-14:i]
    # print()
    if len(set([t for t in letters])) == 14:
        print(i)
        break


