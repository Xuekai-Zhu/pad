def solution():
    """Nancy buys 2 coffees a day. She grabs a double espresso for $3.00 every morning. In the afternoon, she grabs an iced coffee for $2.50. After 20 days, how much money has she spent on coffee?"""
    # Define the cost of the double espresso and iced coffee
    ESPRESSO_PRICE = 3.00
    ICED_COFFEE_PRICE = 2.50

    # Define the number of coffees Nancy buys per day
    coffees_per_day = 2

    # Calculate the total cost of the double espressos for 20 days
    espresso_cost = ESPRESSO_PRICE * coffees_per_day * 20

    # Calculate the total cost of the iced coffees for 20 days
    iced_coffee_cost = ICED_COFFEE_PRICE * coffees_per_day * 20

    # Calculate the total cost of all the coffees
    total_cost = espresso_cost + iced_coffee_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())