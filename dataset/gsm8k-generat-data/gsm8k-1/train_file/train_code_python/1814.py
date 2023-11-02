def solution():
    """Jim has 2 rows of 4 trees to start. When he turns 10 he decides to plant a new row of trees every year on his birthday. On his 15th birthday after he doubles the number of trees he has. How many trees does he have?"""
    initial_trees = 2 * 4 # 2 rows of 4 trees
    trees_planted = 15 - 10 # Jim starts planting trees at age 10
    trees_total = initial_trees + trees_planted * 4 # Jim plants 1 new row of 4 trees each year
    trees_total *= 2 # Jim doubles the number of trees on his 15th birthday
    result = trees_total
    return result

print(solution())