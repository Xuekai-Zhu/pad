def solution():
    coffee_machine_price = 200
    discount = 20
    coffee_price_per_day = 3
    coffee_price_previous = 4
    num_coffees_previous = 2

    # Calculate the discounted price of the coffee machine
    discounted_price = coffee_machine_price - discount

    # Calculate the amount James saves per day by making his own coffee
    savings_per_day = (num_coffees_previous * coffee_price_previous) - (coffee_price_per_day * num_coffees_previous)

    # Calculate the number of days it will take for the coffee machine to pay for itself
    days = discounted_price / savings_per_day
    result = days
    return result

print(solution())