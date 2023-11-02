def solution():
    """Whenever Katie and her family eat donuts, they need some coffee to dunk them in. She notices that for each donut they need 2 ounces of coffee. Every pot of coffee she makes contains 12 ounces and costs $3 to make. If her family finishes 3 dozen donuts, how much do they spend on coffee?"""
    # Define the amount of coffee needed per donut and per pot
    COFFEE_PER_DONUT = 2
    COFFEE_PER_POT = 12

    # Define the number of donuts and pots of coffee needed
    donut_count = 3 * 12 # 3 dozen donuts
    coffee_needed = donut_count * COFFEE_PER_DONUT
    pots_needed = coffee_needed // COFFEE_PER_POT
    if coffee_needed % COFFEE_PER_POT != 0:
        pots_needed += 1

    # Calculate the cost of the coffee
    coffee_cost = pots_needed * 3

    # Display the cost of the coffee
    result = coffee_cost
    return result

print(solution())