def solution():
    # Calculate the total cost of the coffee machine after the discount
    coffee_machine_cost = 200 - 20

    # Calculate how much James spent on coffee per day before buying the machine
    coffee_cost_per_day = 2 * 4

    # Calculate the daily savings from making his own coffee
    daily_savings = coffee_cost_per_day - 3

    # Calculate how many days it will take for the machine to pay for itself
    days_to_pay_off = coffee_machine_cost / daily_savings

    result = days_to_pay_off
    return result

print(solution())