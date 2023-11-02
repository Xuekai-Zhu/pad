def solution():
    # Define the cost of each size duck
    regular_cost = 3
    large_cost = 5
    
    # Calculate the total amount of money raised
    total_regular_cost = regular_cost * 221
    total_large_cost = large_cost * 185
    total_money_raised = total_regular_cost + total_large_cost
    
    result = total_money_raised
    return result

print(solution())