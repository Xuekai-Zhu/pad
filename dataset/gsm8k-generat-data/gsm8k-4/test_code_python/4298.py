def solution():
    """Peter carried $500 to the market. He bought 6 kilos of potatoes for $2 per kilo, 9 kilos of tomato for $3 per kilo, 5 kilos of cucumbers for $4 per kilo, and 3 kilos of bananas for $5 per kilo. How much is Peter’s remaining money?"""
    # Define the initial amount of money Peter carried to the market
    initial_amount = 500

    # Calculate the amount spent on potatoes
    potatoes_cost = 6 * 2

    # Calculate the amount spent on tomatoes
    tomatoes_cost = 9 * 3

    # Calculate the amount spent on cucumbers
    cucumbers_cost = 5 * 4

    # Calculate the amount spent on bananas
    bananas_cost = 3 * 5

    # Calculate the total amount spent
    total_spent = potatoes_cost + tomatoes_cost + cucumbers_cost + bananas_cost

    # Calculate the remaining amount
    remaining_amount = initial_amount - total_spent

    # Return the remaining amount
    result = remaining_amount
    return result

print(solution())