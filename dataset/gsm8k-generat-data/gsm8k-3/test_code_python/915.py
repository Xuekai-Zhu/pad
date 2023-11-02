def solution():
    """A sixty bulb watt uses 60 watts of power each day. If Allyn has 40 such bulbs in his house and pays an electricity bill of twenty cents per power watt used, calculate Allyn's total monthly expenses on electricity in June."""
    # Calculate the total power used by all the bulbs in a day
    total_power = 60 * 40

    # Calculate the total power used in June
    total_power_june = total_power * 30

    # Calculate the total cost in June
    total_cost_june = total_power_june * 0.20

    # Display the total cost in June
    result = total_cost_june
    return result

print(solution())