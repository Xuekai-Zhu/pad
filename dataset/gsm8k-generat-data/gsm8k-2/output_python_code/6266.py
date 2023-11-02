def solution():
    """Mia is a student. In her final year, she spent 1/5 of her day watching TV and 1/4 of the time left on studying. How many minutes did she spend studying each day?"""
    total_minutes = 24 * 60  # minutes in a day
    tv_time = total_minutes / 5
    remaining_time = total_minutes - tv_time
    study_time = remaining_time / 4
    result = study_time
    return result

print(solution())