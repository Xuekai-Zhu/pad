def solution():
    drip_coffee_price = 2.25
    double_shot_espresso_price = 3.50
    latte_price = 4.00
    vanilla_syrup_price = 0.50
    cold_brew_coffee_price = 2.50
    cappuccino_price = 3.50

    num_drip_coffees = 2
    num_double_shot_espressos = 1
    num_lattes = 2
    has_vanilla_syrup = True
    num_cold_brew_coffees = 2
    num_cappuccinos = 1

    # Calculate total cost of drip coffees
    total_drip_coffee_cost = num_drip_coffees * drip_coffee_price

    # Calculate total cost of double shot espressos
    total_double_shot_espresso_cost = num_double_shot_espressos * double_shot_espresso_price

    # Calculate total cost of lattes
    total_latte_cost = num_lattes * latte_price

    # Add cost of vanilla syrup if applicable
    if has_vanilla_syrup:
        total_latte_cost += vanilla_syrup_price

    # Calculate total cost of cold brew coffees
    total_cold_brew_coffee_cost = num_cold_brew_coffees * cold_brew_coffee_price

    # Calculate total cost of cappuccinos
    total_cappuccino_cost = num_cappuccinos * cappuccino_price

    # Calculate total cost of coffee order
    total_cost = (
        total_drip_coffee_cost
        + total_double_shot_espresso_cost
        + total_latte_cost
        + total_cold_brew_coffee_cost
        + total_cappuccino_cost
    )
    result = total_cost
    return result

print(solution())