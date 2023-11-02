def solution():
    
    initial_apples = 10
    initial_oranges = 5
    new_oranges = 5
    total_fruit = initial_apples + initial_oranges + new_oranges
    apple_fraction = initial_apples / total_fruit
    apple_percentage = apple_fraction * 100
    result = apple_percentage
    return result

print(solution())