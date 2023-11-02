def solution():
    """Steve spends 1/3 of the day sleeping, 1/6 of the day in school, 1/12 of the day making assignments, and the rest of the day with his family.
    How many hours does Steve spend with his family in a day?"""
    total_parts = 1 + 1/3 + 1/6 + 1/12
    hours_in_day = 24
    family_time = hours_in_day * (1 - total_parts)
    result = family_time
    return result

print(solution())