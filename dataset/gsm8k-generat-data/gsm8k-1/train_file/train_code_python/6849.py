def solution():
    """Dave breaks 2 guitar strings per night when playing live. If he performs 6 shows a week for 12 weeks, how many guitar strings will he need to replace?"""
    strings_per_night = 2
    shows_per_week = 6
    weeks = 12
    total_strings = strings_per_night * shows_per_week * weeks
    result = total_strings
    return result

print(solution())