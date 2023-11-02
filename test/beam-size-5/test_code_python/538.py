def solution():
    
    apple_price = 1.5
    orange_price = 0.8
    peach_price = 0.75
    num_apples = 3
    num_oranges = 5
    num_peaches = 6
    total_cost = (apple_price * num_apples) + (orange_price * num_oranges) + (peach_price * num_peaches)
    change = 20 - total_cost
    result = change
    return result

print(solution())