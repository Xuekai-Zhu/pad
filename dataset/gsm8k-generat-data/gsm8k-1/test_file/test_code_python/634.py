def solution():
    """In a grocery store, four apples cost $5.20, and three oranges cost $3.30. How much will Clyde pay for 5 apples and 5 oranges?"""
    cost_of_four_apples = 5.20
    cost_of_three_oranges = 3.30
    
    cost_of_one_apple = cost_of_four_apples / 4
    cost_of_one_orange = cost_of_three_oranges / 3
    
    total_cost = (5 * cost_of_one_apple) + (5 * cost_of_one_orange)
    
    result = total_cost
    return result

print(solution())