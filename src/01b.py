

# f = open("data/01.txt", "r")
# lines = print(f.readlines())
with open("data/01.txt", "r") as f:
    lines = f.read().splitlines() 


cumsum = 0
l_sums = []



for l in lines:
    if len(l) == 0:
        l_sums.append(cumsum) 
        cumsum =0
    else:
        cumsum += int(l)

l_sums.sort()
sum(l_sums[-3:])

