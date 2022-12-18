

# f = open("data/01.txt", "r")
# lines = print(f.readlines())
with open("data/01.txt", "r") as f:
    lines = f.read().splitlines() 


cumsum = 0
cummax = 0



for l in lines:
    if len(l) == 0:
        cummax = max(cumsum, cummax)
        cumsum =0
    else:
        cumsum += int(l)

print(cummax)

