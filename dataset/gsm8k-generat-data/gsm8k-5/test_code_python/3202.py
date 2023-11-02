def solution():
    hours = 6  # Milly usually hires the babysitter for 6 hours
    original_cost = 16 * hours  # Milly's current babysitter charges $16/hour
    new_hourly_rate = 12  # The new babysitter charges $12/hour
    extra_fee_per_scream = 3  # The new babysitter charges an extra $3 for each time the kids scream

    # Calculate the total cost of the new babysitter
    new_hourly_cost = new_hourly_rate * hours
    number_of_screams = 2  # Milly's kids usually scream twice per babysitting gig
    extra_scream_fee = extra_fee_per_scream * number_of_screams
    new_total_cost = new_hourly_cost + extra_scream_fee

    # Calculate how much less the new babysitter will cost
    savings = original_cost - new_total_cost
    result = savings
    return result

print(solution())