def solution():
    """It’s Meghan’s turn to pick up her team's coffee order.  She needs 2 drip coffees that are $2.25 each and one double shot espresso that’s $3.50.  She needs 2 lattes that are $4.00 and needs to add vanilla syrup to one of those for an additional $0.50.  She also needs 2 cold brew coffees that are $2.50 each and 1 cappuccino for $3.50.  How much is the coffee order?"""
    # Define the cost of each item
    DRIP_COFFEE_PRICE = 2.25
    ESPRESSO_PRICE = 3.50
    LATTE_PRICE = 4.00
    VANILLA_SYRUP_PRICE = 0.50
    COLD_BREW_COFFEE_PRICE = 2.50
    CAPPUCCINO_PRICE = 3.50

    # Define the number of each item ordered
    drip_coffees = 2
    double_shot_espresso = 1
    lattes = 2
    vanilla_latte = 1
    cold_brew_coffees = 2
    cappuccino = 1

    # Calculate the cost of the drip coffees
    drip_coffee_cost = drip_coffees * DRIP_COFFEE_PRICE

    # Calculate the cost of the double shot espresso
    espresso_cost = double_shot_espresso * ESPRESSO_PRICE

    # Calculate the cost of the lattes
    latte_cost = lattes * LATTE_PRICE

    # Add the cost of vanilla syrup if applicable
    if vanilla_latte == 1:
        latte_cost += VANILLA_SYRUP_PRICE

    # Calculate the cost of the cold brew coffees
    cold_brew_coffee_cost = cold_brew_coffees * COLD_BREW_COFFEE_PRICE

    # Calculate the cost of the cappuccino
    cappuccino_cost = cappuccino * CAPPUCCINO_PRICE

    # Calculate the total cost of the coffee order
    total_cost = drip_coffee_cost + espresso_cost + latte_cost + cold_brew_coffee_cost + cappuccino_cost

    # Display the total cost of the coffee order
    result = total_cost
    return result

print(solution())