def solution():
    # Speed on Monday
    speed_monday = 10  # Harry ran 10 meters per hour on Monday

    # Speed from Tuesday to Thursday
    speed_tuesday_thursday = speed_monday * 1.5  # Harry ran 50% faster than Monday

    # Speed on Friday
    speed_friday = speed_tuesday_thursday * 1.6  # Harry ran 60% faster than Thursday

    result = speed_friday
    return result

print(solution())