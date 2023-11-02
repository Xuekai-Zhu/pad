def solution():
    # Calculate the cost of the drip coffees
    drip_coffee_cost = 2 * 2.25

    # Calculate the cost of the double shot espresso
    double_shot_espresso_cost = 3.50

    # Calculate the cost of the lattes
    regular_latte_cost = 2 * 4
    latte_with_vanilla_cost = 4 + 0.50

    # Calculate the cost of the cold brews
    cold_brew_cost = 2 * 2.50

    # Calculate the cost of the cappuccino
    cappuccino_cost = 3.50

    # Calculate the total cost of the order
    total_cost = drip_coffee_cost + double_shot_espresso_cost + regular_latte_cost + latte_with_vanilla_cost + cold_brew_cost + cappuccino_cost

    result = total_cost
    return result

print(solution())