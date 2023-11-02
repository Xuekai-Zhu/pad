def solution():
    coffees_per_day = 2  # Nancy buys 2 coffees a day
    cost_of_espresso = 3.00  # The cost of a double espresso is $3.00
    cost_of_iced_coffee = 2.50  # The cost of an iced coffee is $2.50
    days = 20  # Nancy has been buying coffee for 20 days

    # Calculate the total amount spent on double espressos
    total_cost_of_espresso = cost_of_espresso * coffees_per_day * days

    # Calculate the total amount spent on iced coffees
    total_cost_of_iced_coffee = cost_of_iced_coffee * coffees_per_day * days

    # Calculate the total amount spent on coffee
    total_cost_of_coffee = total_cost_of_espresso + total_cost_of_iced_coffee
    result = total_cost_of_coffee
    return result

print(solution())