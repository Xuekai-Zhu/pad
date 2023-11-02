def solution():
    """Nancy buys 2 coffees a day. She grabs a double espresso for $3.00 every morning. In the afternoon, she grabs an iced coffee for $2.50. After 20 days, how much money has she spent on coffee?"""
    # Define the cost of each type of coffee
    ESPRESSO_COST = 3.00
    ICED_COFFEE_COST = 2.50

    # Calculate the total cost of coffee for 20 days
    total_cost = 20 * (2 * ESPRESSO_COST + 2 * ICED_COFFEE_COST)

    # Return the total cost
    result = total_cost
    return result

print(solution())