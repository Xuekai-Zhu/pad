def solution():
    """Jason has a carriage house that he rents out. He’s charging $50.00 per day or $500.00 for 14 days. Eric wants to rent the house for 20 days. How much will it cost him?"""
    # Define the daily rental cost and the cost for 14 days
    daily_cost = 50
    fortnight_cost = 500

    # Calculate the cost for 20 days
    if 20 <= 14:
        total_cost = (20 * daily_cost)
    else:
        extra_days = 20 - 14
        total_cost = fortnight_cost + (extra_days * daily_cost)

    # return the result
    result = total_cost
    return result

print(solution())