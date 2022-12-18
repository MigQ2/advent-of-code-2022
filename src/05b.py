

with open("data/05.txt", "r") as f:
    lines = f.read().splitlines() 



# l = lines[15]
done_boxes = 0
width = 0
for l in lines:
    if width == 0:
        width = int(len(l) / 4) +1
        stacks = [[] for i in range(width)]
    # if l[0] == " ":
    #     done_boxes = 1
    #     if l[1] == "1":
    #         width = int(max([c for c in l]))
    #         print(f"Width {width}")
    #     continue
    if l.startswith("move"):
        # if done_boxes == 0:
        print(stacks)
        done_boxes = 1
        print(l)
        n_crates, from_pos, to_pos = [int(i) for i in l.split(" ") if i in [str(i) for i in range(100)]]
        from_pos = from_pos-1
        to_pos = to_pos-1
        moved_crates = stacks[from_pos][:n_crates]
        # moved_crates.reverse()
        stacks[to_pos] = moved_crates + stacks[to_pos] 
        stacks[from_pos] = stacks[from_pos][n_crates:]

    if done_boxes == 0:
        l = " " + l
        for i in range(width):
            box = l[4*i +1: 4*i +4]
            if box.startswith("["):
                stacks[i] += box[1]

res = [stacks[i][0] for i  in range(width)]
strin = ""
for i in res:
    strin += i
print(strin)








