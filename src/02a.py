

with open("data/02.txt", "r") as f:
    lines = f.read().splitlines() 

l = lines[2]

score = 0

for l in lines:
    opp, me = l.split(" ")

    opp_dict ={
        "A" :1,
        "B" :2,
        "C" :3,
    }
    me_dict ={
        "X" :1,
        "Y" :2,
        "Z" :3,
    }

    score+=me_dict[me]

    diff = (me_dict[me] - opp_dict[opp]) % 3
    if diff == 0:
        score +=3
    if diff == 1:
        score += 6 
    # print(score)

print(score)
