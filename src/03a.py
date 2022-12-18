

with open("data/03.txt", "r") as f:
    lines = f.read().splitlines() 

l = lines[0]
score = 0

for l in lines:

    r1 = l[:int(len(l)/2)]
    r2 = l[int(len(l)/2):]

    common_l = list(set([c for c in r1]).intersection(set([c for c in r2])))
    assert len(common_l) == 1
    common = common_l[0]

    if common == common.lower():
        score += ord(common) - ord("a") + 1
    else: 
        score += ord(common) - ord("A") + 27

    # ord("P") - ord("a") + 1

print(score)