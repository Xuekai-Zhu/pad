def solution():
    """Your video streaming subscription costs $14 a month. If you're evenly splitting the cost with your friend, how much do you pay in total after the first year for this service?"""
    subscription_cost = 14
    months_in_year = 12
    total_cost = subscription_cost * months_in_year
    cost_per_person = total_cost / 2
    result = cost_per_person
    return result

print(solution())