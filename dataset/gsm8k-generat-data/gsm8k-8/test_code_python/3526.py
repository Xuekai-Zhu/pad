def solution():
    # Calculate the cost of 1 apple and 1 orange
    cost_per_apple = 2 / 10
    cost_per_orange = 1.5 / 5
    
    # Determine which fruit is cheaper
    if cost_per_apple < cost_per_orange:
        cost_per_fruit = cost_per_apple
    else:
        cost_per_fruit = cost_per_orange
    
    # Calculate the cost of 12 fruits
    cost = 12 * cost_per_fruit * 100   # multiply by 100 to convert to cents
    
    result = cost
    return result

print(solution())