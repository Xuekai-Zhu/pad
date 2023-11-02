def solution():
    """In a family of 5, three people eat three eggs each day while the rest eat two eggs each day. If they eat eggs every day, how many eggs will the family consume in a week?"""
    total_people = 5
    eggs_per_day = (3 * 3) + ((total_people - 3) * 2)
    eggs_per_week = eggs_per_day * 7
    result = eggs_per_week
    return result

print(solution())