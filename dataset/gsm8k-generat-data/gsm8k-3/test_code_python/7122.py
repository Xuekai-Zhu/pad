def solution():
    """Mark bought 2 pounds of tomatoes for $5 per pound and 5 pounds of apples, at $6 per pound. How much did he spend in total?"""
    # Define the price per pound of tomatoes and apples
    TOMATO_PRICE = 5
    APPLE_PRICE = 6

    # Define the number of pounds of tomatoes and apples
    tomato_pounds = 2
    apple_pounds = 5

    # Calculate the total cost of the tomatoes
    tomato_cost = tomato_pounds * TOMATO_PRICE

    # Calculate the total cost of the apples
    apple_cost = apple_pounds * APPLE_PRICE

    # Calculate the total cost of the purchase
    total_cost = tomato_cost + apple_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())