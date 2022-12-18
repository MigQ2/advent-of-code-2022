from pathlib import Path


with open("data/07.txt", "r") as f:
    lines = f.read().splitlines() 

current_dir = "/"
files = {}


l = lines[0]
for l in lines:
    if l.startswith("$ cd /"):
        current_dir = "/"
    elif l.startswith("$ cd .."):
        current_dir = str(Path(current_dir).parent.absolute())
        if not current_dir.endswith("/"):
            current_dir = current_dir + "/"
    elif l.startswith("$ cd"):
        current_dir = current_dir + l.split(" ")[-1] + "/"
    elif l.startswith("$ ls"):
        pass
        # current_ls = l.split(" ")[:1]
    elif l.startswith("dir"):
        key = current_dir# + "/" + current_ls
        if key not in files.keys():
            files[key] = {}
        files[key][current_dir + l.split(" ")[-1] + "/"] = "dir"
    else:
        key = current_dir# + "/" + current_ls
        if key not in files.keys():
            files[key] = {}
        files[key][l.split(" ")[-1]] = int(l.split(" ")[0])

# print(files)

def getsize(d, files):
    total = 0
    for subdir, val in files[d].items():
        if val == "dir":
            total += getsize(subdir, files)
        else:
            total += val
    return total

score = 0
for subdir in files.keys():
    size = getsize(subdir, files)
    if size <= 100000:
        score += size

files.keys()

print(score)
# getsize('/',files)
