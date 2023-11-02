def solution():
    """John plants a plot of 3 trees by 4 trees. Each tree gives 5 apples. He sells each apple for $.5.
    How much money does he make, in dollars?"""
    trees_length = 3
    trees_width = 4
    trees_planted = trees_length * trees_width
    apples_per_tree = 5
    total_apples = trees_planted * apples_per_tree
    price_per_apple = 0.5
    money_made = total_apples * price_per_apple
    result = money_made
    return result

print(solution())