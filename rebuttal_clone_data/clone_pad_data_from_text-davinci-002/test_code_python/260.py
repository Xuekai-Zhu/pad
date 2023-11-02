def solution():
    """Every hour past noon shadows from a building stretch an extra 5 feet, starting at zero at noon. How long are the shadows from the building 6 hours past noon in inches?"""
    hours_since_noon = 6
    feet_per_hour = 5
    inches_per_foot = 12
    total_inches = hours_since_noon * feet_per_hour * inches_per_foot
    result = total_inches
    return result

print(solution())