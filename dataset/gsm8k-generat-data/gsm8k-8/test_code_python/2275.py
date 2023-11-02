def solution():
    apples_bought = 6

    # Calculate the number of trees planted from each apple
    trees_planted_per_apple = 2

    # Calculate the total number of trees planted
    total_trees_planted = (apples_bought * trees_planted_per_apple) - apples_bought

    # Calculate the number of apples Mary ate
    apples_ate = apples_bought - total_trees_planted

    result = apples_ate
    return result

print(solution())