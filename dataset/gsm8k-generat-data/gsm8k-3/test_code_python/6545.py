def solution():
    """James decides to start making his own coffee.  He buys a coffee machine for $200 and gets a $20 discount.  He figures it will cost him $3 a day to make his coffee.  He previously bought 2 coffees a day for $4 each.   How long until the machine pays for itself?"""
    # Calculate the total cost of the coffee machine after discount
    machine_cost = 200 - 20

    # Calculate James' daily savings after starting to make his own coffee
    daily_savings = (2 * 4) - (2 * 3)

    # Calculate the number of days it will take for the coffee machine to pay for itself
    days_to_pay_off = machine_cost / daily_savings

    # Display the number of days it will take
    result = days_to_pay_off
    return result

print(solution())