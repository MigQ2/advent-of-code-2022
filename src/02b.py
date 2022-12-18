

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
    win_dict ={
        "X" :-1,
        "Y" : 0,
        "Z" : 1,
    }

    score += (((opp_dict[opp]-1) + win_dict[me]) % 3) +1
    
    score+=(me_dict[me]-1) * 3


print(score)
