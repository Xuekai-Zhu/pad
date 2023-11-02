def solution():
    """Jason has a carriage house that he rents out. He's charging $50.00 per day or $500.00 for 14 days. Eric wants to rent the house for 20 days. How much will it cost him?"""
    daily_rate = 50
    weekly_rate = 500
    days_in_week = 14
    if days_in_week < 20:
        # Eric will need to pay for one full week and some extra days
        weeks = 1
        extra_days = 20 - days_in_week
    else:
        # Eric can pay for two full weeks
        weeks = 2
        extra_days = 0

    total_cost = weekly_rate * weeks  # cost of whole weeks
    total_cost += extra_days * daily_rate  # cost of remaining days
    result = total_cost
    return result

print(solution())