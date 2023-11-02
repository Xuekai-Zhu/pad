def solution():
    # Calculate the height of the papaya tree in each year
    year_1_height = 2  # the tree grows 2 feet in the first year
    year_2_height = year_1_height * 1.5  # the tree grows 50% more than in the first year
    year_3_height = year_2_height * 1.5  # the tree grows 50% more than in the second year
    year_4_height = year_3_height * 2  # the tree grows twice as much as in the third year
    year_5_height = year_4_height * 0.5  # the tree grows half as much as in the fourth year

    # Calculate the total height of the tree after 5 years
    total_height = year_1_height + year_2_height + year_3_height + year_4_height + year_5_height
    result = total_height
    return result

print(solution())