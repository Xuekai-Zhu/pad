def solution():
    """Mark bought 2 pounds of tomatoes for $5 per pound and 5 pounds of apples, at $6 per pound. How much did he spend in total?"""
    # Define the prices and quantities of tomatoes and apples
    tomato_price = 5
    tomato_quantity = 2
    apple_price = 6
    apple_quantity = 5

    # Calculate the total cost of tomatoes and apples
    total_cost = (tomato_price * tomato_quantity) + (apple_price * apple_quantity)

    result = total_cost
    return result

print(solution())