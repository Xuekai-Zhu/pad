def solution():
    initial_rows = 2
    trees_per_row = 4
    new_rows_after_10th_birthday = 5
    new_trees_per_year = 4

    # Calculate the number of trees planted in the first 10 years
    trees_planted_in_first_10_years = (initial_rows + new_rows_after_10th_birthday) * trees_per_row

    # Calculate the number of trees planted after the 10th birthday
    trees_planted_after_10th_birthday = (15 - 10) * new_trees_per_year

    # Calculate the total number of trees after doubling
    total_trees = (trees_planted_in_first_10_years + trees_planted_after_10th_birthday) * 2
    result = total_trees
    return result

print(solution())