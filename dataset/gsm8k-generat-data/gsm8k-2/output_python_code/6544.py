def solution():
    """James decides to start making his own coffee. He buys a coffee machine for $200 and gets a $20 discount. He figures it will cost him $3 a day to make his coffee. He previously bought 2 coffees a day for $4 each. How long until the machine pays for itself?"""
    machine_cost = 200 - 20
    daily_savings = (2 * 4) - (3 * 2) # savings per day by making own coffee
    days_to_break_even = machine_cost / daily_savings
    result = days_to_break_even
    return result

print(solution())