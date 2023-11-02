def solution():
    """Ducks need to eat 3.5 pounds of insects each week to survive. If there is a flock of ten ducks, how many pounds of insects do they need per day?"""
    pounds_per_week = 3.5
    ducks_in_flock = 10
    pounds_per_day = pounds_per_week / 7 * ducks_in_flock
    result = pounds_per_day
    return result

print(solution())