

with open("data/04.txt", "r") as f:
    lines = f.read().splitlines() 

score = 0

l = lines[0]
for l in lines:

    l1,l2 = l.split(",")

    min_1,max_1 = [int(i) for i in l1.split("-")]
    min_2,max_2 = [int(i) for i in l2.split("-")]

    if (min_1 <= min_2) and (max_1>=max_2):
        score += 1
    elif (min_2 <= min_1) and (max_2>=max_1):
        score += 1


print(score)