def solution():
    """George bought some food for his trip: a bottle of juice, a sandwich, and a bottle of milk. The sandwich was for $4, and the juice was two times more expensive. The bottle of milk cost was 75% of the total cost of the sandwich and juice. How much did George pay for his food?"""
    # Define the price of the sandwich
    sandwich_price = 4

    # Calculate the price of the juice
    juice_price = sandwich_price * 2

    # Calculate the total cost of the sandwich and juice
    sandwich_juice_cost = sandwich_price + juice_price

    # Calculate the cost of the bottle of milk
    milk_cost = 0.75 * sandwich_juice_cost

    # Calculate the total cost of the food
    total_cost = sandwich_price + juice_price + milk_cost

    # Return the result
    result = total_cost
    return result

print(solution())