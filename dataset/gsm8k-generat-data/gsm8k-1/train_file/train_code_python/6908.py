def solution():
    """If 8 carpenters can make 50 chairs in 10 days, how many carpenters are needed to make 75 chairs in 10 days?"""
    carpenters_per_chair_per_day = 0.2
    chairs_per_day = 5
    days = 10
    chairs_needed = 75
    carpenters_needed = (chairs_needed / chairs_per_day) / (days * carpenters_per_chair_per_day)
    result = round(carpenters_needed)
    return result

print(solution())