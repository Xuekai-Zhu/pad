def solution():
    """John plants a plot of 3 trees by 4 trees. Each tree gives 5 apples. He sells each apple for $.5. How much money does he make, in dollars?"""
    num_trees = 3 * 4
    apples_per_tree = 5
    total_apples = num_trees * apples_per_tree
    apple_price = 0.5
    total_earnings = total_apples * apple_price
    result = total_earnings
    return result

print(solution())