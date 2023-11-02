def solution():
    num_trees = 3 * 4  # John plants a plot of 3 trees by 4 trees, so there are 12 trees
    num_apples = num_trees * 5  # Each tree gives 5 apples, so there are 60 apples

    # Calculate the total amount of money John makes by selling the apples
    total_money = num_apples * 0.5  # John sells each apple for $.5

    result = total_money
    return result

print(solution())