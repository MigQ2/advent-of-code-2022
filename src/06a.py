

with open("data/06.txt", "r") as f:
    lines = f.read().splitlines() 

l = lines[0]
# for l in lines:

for i in range(4, len(l)):
    letters = l[i-4:i]
    # print()
    if len(set([t for t in letters])) == 4:
        print(i)
        break


