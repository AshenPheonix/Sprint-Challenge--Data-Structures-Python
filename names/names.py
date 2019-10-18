import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# removed for stetch
# BST = BinarySearchTree(names_1[0])
# names_1 = names_1[1:]
# 
# for name in names_1:
#     BST.insert(name)

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_1+=names_2
names_1.sort()
for i in range(len(names_1)-1):
    if names_1[i] == names_1[i+1]:
        duplicates.append(names_1[i])


# removed for stretch
# for name in names_2:
#     BST.insert(name)


# removed for stretch 
# BST.get_copies(duplicates)

# Basic runtime is O(N**2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# for Stretch


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

