def solution():
    """George bought some food for his trip: a bottle of juice, a sandwich, and a bottle of milk. The sandwich was for $4, and the juice was two times more expensive. The bottle of milk cost was 75% of the total cost of the sandwich and juice. How much did George pay for his food?"""
    sandwich_cost = 4
    juice_cost = 2 * sandwich_cost
    total_cost = sandwich_cost + juice_cost
    milk_cost = 0.75 * total_cost
    total_food_cost = milk_cost + total_cost
    result = total_food_cost
    return result

print(solution())