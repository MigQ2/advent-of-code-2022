
import numpy as np


with open("data/08.txt", "r") as f:
    lines = f.read().splitlines() 
all_l = []

# l = lines[0]
for l in lines:
    all_l += [[int(i) for i in l]]

mat = np.matrix(all_l)
mat.shape

n_visible = 0

for i in range(len(mat)):
    for j in range(len(mat)):
        if i==0 or j==0 or i == (len(mat)-1) or j == (len(mat)-1):
            n_visible+= 1
            continue
        if np.max(mat[:i, j]) < mat[i,j]:
            n_visible+= 1
            continue
        if np.max(mat[i, :j]) < mat[i,j]:
            n_visible+= 1
            continue
        if np.max(mat[i+1:, j]) < mat[i,j]:
            n_visible+= 1
            continue
        if np.max(mat[i, j+1:]) < mat[i,j]:
            n_visible+= 1
            continue

print(n_visible)




