def solution():
    """There are 40 Judges in the state of Rhode Island. 10 percent of Judges are under 30 years old.
    60 percent of Judges are 30-50 years old. The rest of the Judges are over 50 years old.
    How many Judges are over 50 years old?"""
    total_judges = 40
    under_30 = int(total_judges * 0.1)
    from_30_to_50 = int(total_judges * 0.6)
    over_50 = total_judges - under_30 - from_30_to_50
    result = over_50
    return result

print(solution())