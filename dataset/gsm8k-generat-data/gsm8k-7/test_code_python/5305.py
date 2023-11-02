def solution():
    apple_pie_cost = 12
    cheesecake_1_cost = apple_pie_cost * 0.75  # 25% discount
    muffins_cost = cheesecake_1_cost * 2  # twice the cost of one cheesecake
    
    # Total cost of all items
    total_cost = (2 * cheesecake_1_cost) + apple_pie_cost + muffins_cost
    
    result = total_cost
    return result

print(solution())