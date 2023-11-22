def solution():
    
    # Define the prices of each fruit
    APPLE_PRICE = 0.5
    BANANA_PRICE = APPLE_PRICE * 2
    ORANGE_PRICE = BANANA_PRICE * 3

    # Define the quantities of each fruit
    bananas = 5
    apples = 12
    oranges = 7

    # Calculate the total cost of the fruit
    total_cost = (bananas * BANANA_PRICE) + (apples * APPLE_PRICE) + (oranges * ORANGE_PRICE)

    # Display the total cost
    result = total_cost
    return result

print(solution())