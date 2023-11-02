def solution():
    
    apple_cost = 2
    banana_cost = 1
    orange_cost = 3
    num_apples = 12
    num_bananas = 4
    num_oranges = 4
    total_cost = (apple_cost * num_apples) + (banana_cost * num_bananas) + (orange_cost * num_oranges)
    num_fruit = num_apples + num_bananas + num_oranges
    avg_cost = total_cost / num_fruit
    result = avg_cost
    return result

print(solution())