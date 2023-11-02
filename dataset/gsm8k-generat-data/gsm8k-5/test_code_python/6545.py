def solution():
    coffee_machine_cost = 200 - 20  # James buys a coffee machine for $200 with a $20 discount
    daily_coffee_cost = 3  # James figures it will cost him $3 a day to make his own coffee
    daily_savings = 8  # James previously bought 2 coffees a day for $4 each, so he saves $8 per day

    # Calculate the number of days it will take for the machine to pay for itself
    days_to_recover_cost = coffee_machine_cost / (daily_savings - daily_coffee_cost)
    result = days_to_recover_cost
    return result

print(solution())