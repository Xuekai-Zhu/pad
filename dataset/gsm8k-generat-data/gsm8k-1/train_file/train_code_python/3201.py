def solution():
    """Milly's babysitter charges $16/hour. Milly is considering switching to a new babysitter who charges $12/hour, but also charges an extra $3 for each time the kids scream at her. If Milly usually hires the babysitter for 6 hours, and her kids usually scream twice per babysitting gig, how much less will the new babysitter cost?"""
    current_rate = 16
    new_rate = 12
    extra_charge = 3
    hours_per_day = 6
    screams_per_day = 2
    current_cost = current_rate * hours_per_day
    new_cost = new_rate * hours_per_day + screams_per_day * extra_charge
    savings_per_day = current_cost - new_cost
    result = savings_per_day
    return result

print(solution())