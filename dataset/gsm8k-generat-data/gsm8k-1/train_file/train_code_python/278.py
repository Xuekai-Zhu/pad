def solution():
    """One of Robi's new year's resolutions is to start saving. He started to save $2 in January. This is followed by $4 in February and $8 in March. If he continues this saving pattern, how much will be his total savings after 6 months?"""
    jan_savings = 2
    feb_savings = 4
    mar_savings = 8
    savings = jan_savings + feb_savings + mar_savings
    for i in range(3, 7):
        savings = savings * 2
        month_savings = 2 ** (i - 1) * jan_savings
        savings += month_savings
    result = savings
    return result

print(solution())