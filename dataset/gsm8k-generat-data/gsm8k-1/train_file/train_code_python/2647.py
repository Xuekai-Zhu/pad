def solution():
    """The ratio representing the age of Halima, Beckham, and Michelle is 4:3:7, respectively. If the total age for the three siblings is 126, calculate the age difference between Halima and Beckham."""
    total_ratio = 4 + 3 + 7
    halima_age = 4 / total_ratio * 126
    beckham_age = 3 / total_ratio * 126
    age_difference = halima_age - beckham_age
    result = age_difference
    return result

print(solution())