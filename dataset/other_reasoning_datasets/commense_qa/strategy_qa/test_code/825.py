def solution():
    snake_capacity = 130
    tank_weight = "several tons"
    # Check if the snake's capacity is greater than the weight of the tank
    if snake_capacity > tank_weight:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())