
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
max_score = 0
for i in range(len(mat)):
    for j in range(len(mat)):
        if i==0 or j==0 or i == (len(mat)-1) or j == (len(mat)-1):
            n_visible+= 1
            continue

        #UP
        # elems = [int(elem) for elem in mat[:i, j]]
        # elems.reverse()
        # visible_array = np.array(elems) < mat[i,j]
        # up_score = min(np.where(visible_array == False))
        # if len(up_score) == 0:
        #     up_score = len(visible_array)

        # #DOWN
        # elems = [int(elem) for elem in mat[i+1:, j]]
        # # elems.reverse()
        # visible_array = np.array(elems) < mat[i,j]
        # down_score = min(np.where(visible_array == False)[])
        # if len(down_score) == 0:
        #     down_score = len(visible_array)

        # #LEFT
        # elems = list([elem for elem in np.array(mat[i, :j])][0])
        # elems.reverse()
        # visible_array = np.array(elems) < mat[i,j]
        # left_score = min(np.where(visible_array == False))
        # if len(left_score) == 0:
        #     left_score = len(visible_array)

        # #RIGHT
        # elems = list([elem for elem in np.array(mat[i, j+1:])][0])
        # # elems.reverse()
        # visible_array = np.array(elems) < mat[i,j]
        # right_score = min(np.where(visible_array == False))
        # if len(right_score) == 0:
        #     right_score = len(visible_array)

        #UP
        elems = [int(elem) for elem in mat[:i, j]]
        elems.reverse()
        visible_array = np.array(elems) < mat[i,j]
        up_score = [i for i in range(len(visible_array)) if visible_array[i] == False]
        if len(up_score) == 0:
            up_score = len(visible_array) 
        else:
            up_score = min(up_score)+ 1
        # up_score = min(np.where(visible_array == False))
        

        #DOWN
        elems = [int(elem) for elem in mat[i+1:, j]]
        # elems.reverse()
        visible_array = np.array(elems) < mat[i,j]
        # down_score = min(np.where(visible_array == False)[])
        down_score = [i for i in range(len(visible_array)) if visible_array[i] == False]
        if len(down_score) == 0:
            down_score = len(visible_array)
        else:
             down_score = min(down_score)+ 1
        

        #LEFT
        elems = list([elem for elem in np.array(mat[i, :j])][0])
        elems.reverse()
        visible_array = np.array(elems) < mat[i,j]
        # left_score = min(np.where(visible_array == False))
        left_score = [i for i in range(len(visible_array)) if visible_array[i] == False]
        if len(left_score) == 0:
            left_score = len(visible_array)
        else:
             left_score = min(left_score)+ 1
       

        #RIGHT
        elems = list([elem for elem in np.array(mat[i, j+1:])][0])
        # elems.reverse()
        visible_array = np.array(elems) < mat[i,j]
        # right_score = min(np.where(visible_array == False))
        right_score = [i for i in range(len(visible_array)) if visible_array[i] == False]
        if len(right_score) == 0:
            right_score = len(visible_array)
        else:
            right_score = min(right_score)+ 1
       

        total_score = up_score*down_score*left_score*right_score
        if total_score > max_score:
            max_score = total_score
# print(n_visible)

# print(mat)
# i=3
# j=2
# [elem for elem in np.array(mat[i, :j])]


#  np.array(mat[i, :j])


print(max_score)