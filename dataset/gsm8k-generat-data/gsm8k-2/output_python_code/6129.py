def solution():
    """Audrey is 7 years older than Heracles. In 3 years, Audrey will be twice as old as Heracles is now. How old is Heracles now?"""
    age_difference = 7
    audrey_future_age = heracles_age * 2 - 3
    heracles_age = (audrey_future_age - age_difference) / 2
    result = heracles_age
    return result

print(solution())