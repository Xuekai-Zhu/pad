def solution():
    """Last year there were 50 students enrolled in a calligraphy class. This year, there was a 20% increase in enrollment. How many students are enrolled this year in the calligraphy class?"""
    initial_enrollment = 50
    percent_increase = 20
    increase_amount = initial_enrollment * (percent_increase / 100)
    total_enrollment = initial_enrollment + increase_amount
    result = total_enrollment
    return result

print(solution())