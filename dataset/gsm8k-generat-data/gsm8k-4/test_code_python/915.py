def solution():
    """A sixty bulb watt uses 60 watts of power each day. If Allyn has 40 such bulbs in his house and pays an electricity bill of twenty cents per power watt used, calculate Allyn's total monthly expenses on electricity in June."""
    # Define the power used by each bulb per day
    power_per_bulb = 60

    # Define the number of bulbs in Allyn's house
    num_bulbs = 40

    # Calculate the total power used by all the bulbs in one day
    total_power_per_day = power_per_bulb * num_bulbs

    # Calculate the total power used in one month (30 days)
    total_power_per_month = total_power_per_day * 30

    # Calculate the total cost of electricity for one month
    cost_per_watt = 0.20
    total_cost = total_power_per_month * cost_per_watt

    # return the result
    result = total_cost
    return result

print(solution())