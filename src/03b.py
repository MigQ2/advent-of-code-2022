

with open("data/03.txt", "r") as f:
    lines = f.read().splitlines() 

l = lines[0]
score = 0

lines_counter = 0
for l in lines:
    lines_counter +=1
    if (lines_counter %3) == 1:
        r1 = l
        continue
    if (lines_counter %3) == 2:
        r2 = l
        continue
    else:
        r3 = l
    

        common_l = list(set([c for c in r1]).intersection(set([c for c in r2])).intersection(set([c for c in r3])))
        assert len(common_l) == 1
        common = common_l[0]

        if common == common.lower():
            score += ord(common) - ord("a") + 1
        else: 
            score += ord(common) - ord("A") + 27

    # ord("P") - ord("a") + 1

print(score)