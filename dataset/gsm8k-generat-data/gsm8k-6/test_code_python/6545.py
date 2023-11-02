def solution():
    # Calculate the cost of the coffee machine after discounts
    cost_machine = 200 - 20  # coffee machine costs $200 with a $20 discount

    # Calculate the amount of money James spends on coffee per day before buying the machine
    cost_coffee_per_day = 2 * 4  # James spends $4 for 2 coffees per day before buying the machine

    # Calculate the amount of money James saves per day by making his own coffee
    savings_per_day = cost_coffee_per_day - 3  # James spends $3 per day making his own coffee

    # Calculate the number of days it will take for the machine to pay for itself
    days_to_break_even = cost_machine / savings_per_day

    result = days_to_break_even
    return result

print(solution())