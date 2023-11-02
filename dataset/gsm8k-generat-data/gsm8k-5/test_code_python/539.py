def solution():
    trees_chopped = 200 + 300  # The company chopped down 200 trees in the first half and 300 trees in the second half
    trees_planted = trees_chopped * 3  # The company wants to plant three trees for every tree chopped down
    trees_needed = trees_planted - trees_chopped  # The company wants to know how many more trees they need to plant

    result = trees_needed
    return result

print(solution())