def solution():
    """A cattle breeder owns 52 dairy cows. Each cow gives 1000 oz of milk per day. Calculate the amount of milk produced per week by the cows."""
    cows = 52
    milk_per_cow = 1000
    milk_per_week = cows * milk_per_cow * 7
    result = milk_per_week
    return result

print(solution())