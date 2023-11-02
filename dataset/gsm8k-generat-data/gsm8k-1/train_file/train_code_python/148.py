def solution():
    """In 3 years, Jayden will be half of Ernesto's age. If Ernesto is 11 years old, how many years old is Jayden now?"""
    ernesto_age = 11
    time_difference = 3
    jayden_age_in_future = (ernesto_age * 2) - time_difference
    jayden_age_now = jayden_age_in_future - time_difference
    result = jayden_age_now
    return result

print(solution())