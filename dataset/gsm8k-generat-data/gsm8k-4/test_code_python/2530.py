def solution():
    """Whenever Katie and her family eat donuts, they need some coffee to dunk them in. She notices that for each donut they need 2 ounces of coffee. Every pot of coffee she makes contains 12 ounces and costs $3 to make. If her family finishes 3 dozen donuts, how much do they spend on coffee?"""
    # Define the number of donuts and the amount of coffee needed per donut
    num_donuts = 3 * 12
    coffee_per_donut = 2

    # Calculate the total amount of coffee needed
    total_coffee = num_donuts * coffee_per_donut

    # Calculate the number of coffee pots needed
    num_pots = total_coffee // 12 + (1 if total_coffee % 12 != 0 else 0)

    # Calculate the total cost of making coffee
    coffee_cost = num_pots * 3

    # return the result
    result = coffee_cost
    return result

print(solution())