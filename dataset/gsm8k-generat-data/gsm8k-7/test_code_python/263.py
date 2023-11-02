def solution():
    rows = 3
    columns = 4
    apples_per_tree = 5
    price_per_apple = 0.5

    # Calculate the total number of trees planted
    total_trees = rows * columns

    # Calculate the total number of apples produced
    total_apples = total_trees * apples_per_tree

    # Calculate the total revenue from selling apples
    total_revenue = total_apples * price_per_apple
    result = total_revenue
    return result

print(solution())