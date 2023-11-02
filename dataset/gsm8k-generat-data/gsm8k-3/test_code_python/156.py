def solution():
    """George bought some food for his trip: a bottle of juice, a sandwich, and a bottle of milk. The sandwich was for $4, and the juice was two times more expensive. The bottle of milk cost was 75% of the total cost of the sandwich and juice. How much did George pay for his food?"""
    # Define the cost of the sandwich
    sandwich_cost = 4

    # Define the cost of the juice as twice that of the sandwich
    juice_cost = 2 * sandwich_cost

    # Calculate the total cost of the sandwich and juice
    sandwich_juice_cost = sandwich_cost + juice_cost

    # Calculate the cost of the milk as 75% of the total cost of the sandwich and juice
    milk_cost = 0.75 * sandwich_juice_cost

    # Calculate the total cost of the food
    total_cost = sandwich_cost + juice_cost + milk_cost

    # Return the result
    result = total_cost
    return result

print(solution())