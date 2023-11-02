def solution():
    """Steve spends 1/3 of the day sleeping, 1/6 of the day in school, 1/12 of the day making assignments, and the rest of the day with his family. How many hours does Steve spend with his family in a day?"""
    total_time = 24  # hours
    sleeping_time = total_time * (1/3)
    school_time = total_time * (1/6)
    making_assignments_time = total_time * (1/12)
    family_time = total_time - sleeping_time - school_time - making_assignments_time
    result = family_time
    return result

print(solution())