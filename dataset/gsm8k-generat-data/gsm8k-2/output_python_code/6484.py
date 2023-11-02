def solution():
    """My age is five times that of my son. Next year, my son will be eight years old. How old am I now?"""
    son_age_next_year = 8
    son_age_now = son_age_next_year - 1
    my_age_now = 5 * son_age_now
    result = my_age_now
    return result

print(solution())