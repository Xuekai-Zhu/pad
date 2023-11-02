def solution():
    # Calculate the cost of each item Meghan needs to order
    drip_coffee = 2.25
    double_shot_espresso = 3.50
    latte = 4.00
    latte_with_vanilla = 4.50
    cold_brew_coffee = 2.50
    cappuccino = 3.50

    # Calculate the total cost of the coffee order
    total_cost = (2 * drip_coffee) + double_shot_espresso + (2 * latte_with_vanilla) + (2 * cold_brew_coffee) + cappuccino
    result = total_cost
    return result

print(solution())