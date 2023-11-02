def solution():
    """Milly's babysitter charges $16/hour. Milly is considering switching to a new babysitter who charges $12/hour, but also charges an extra $3 for each time the kids scream at her. If Milly usually hires the babysitter for 6 hours, and her kids usually scream twice per babysitting gig, how much less will the new babysitter cost?"""
    # Calculate the cost of the current babysitter
    current_cost = 16 * 6

    # Calculate the cost of the new babysitter, including extra charges for screaming kids
    new_hourly_rate = 12
    new_scream_charge = 3
    new_hours = 6
    new_screams = 2
    new_cost = (new_hourly_rate * new_hours) + (new_screams * new_scream_charge)

    # Calculate the difference in cost
    cost_difference = current_cost - new_cost

    # return the result
    result = cost_difference
    return result

print(solution())