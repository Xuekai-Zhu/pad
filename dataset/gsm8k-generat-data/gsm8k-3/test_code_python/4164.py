def solution():
    """One kilogram of tomatoes is 20% cheaper than one kilogram of cucumbers. One kilogram of cucumbers costs $5. What is the price of two kilograms of tomatoes and three kilograms of cucumbers?"""
    # Define the cost of one kilogram of cucumbers
    CUCUMBER_PRICE = 5

    # Calculate the cost of one kilogram of tomatoes
    TOMATO_PRICE = CUCUMBER_PRICE * 0.8

    # Calculate the total cost of two kilograms of tomatoes
    tomato_cost = TOMATO_PRICE * 2

    # Calculate the total cost of three kilograms of cucumbers
    cucumber_cost = CUCUMBER_PRICE * 3

    # Calculate the total cost of all the vegetables
    total_cost = tomato_cost + cucumber_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())