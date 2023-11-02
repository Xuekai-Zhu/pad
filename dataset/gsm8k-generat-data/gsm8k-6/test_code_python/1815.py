def solution():
    # Calculate the total number of trees Jim has
    trees = 2 * 4  # Jim starts with 2 rows of 4 trees
    trees_per_year = 1  # Jim plants a new row of trees every year on his birthday

    for year in range(10, 15):
        trees += trees_per_year  # Jim plants a new row of trees on his birthday
        if year == 15:
            trees *= 2  # Jim doubles the number of trees on his 15th birthday

    result = trees
    return result

print(solution())