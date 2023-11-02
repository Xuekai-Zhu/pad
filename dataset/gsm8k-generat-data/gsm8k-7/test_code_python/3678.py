def solution():
    starting_height = 5
    growth_rate = 3
    target_height = 23

    # Calculate the number of years it will take for the tree to reach the target height
    total_growth = target_height - starting_height
    years_to_reach = total_growth / growth_rate

    # Calculate the age of the tree when it reaches the target height
    tree_age_at_target_height = years_to_reach + 1  # add 1 to include the starting year

    result = tree_age_at_target_height
    return result

print(solution())