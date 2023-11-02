def solution():
    """One of Robi's new year's resolutions is to start saving. He started to save $2 in January. This is followed by $4 in February and $8 in March. If he continues this saving pattern, how much will be his total savings after 6 months?"""
    month1 = 2
    month2 = 4
    month3 = 8
    month4 = 16
    month5 = 32
    month6 = 64
    total_savings = month1 + month2 + month3 + month4 + month5 + month6
    result = total_savings
    return result

print(solution())