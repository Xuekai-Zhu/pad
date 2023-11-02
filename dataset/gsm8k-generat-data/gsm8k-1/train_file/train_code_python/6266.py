def solution():
    """Mia is a student. In her final year, she spent 1/5 of her day watching TV and 1/4 of the time left on studying. How many minutes did she spend studying each day?"""
    total_minutes = 1440 # total minutes in a day
    tv_time = total_minutes*(1/5)
    study_time = (total_minutes-tv_time)*(1/4)
    result = study_time
    return result

print(solution())