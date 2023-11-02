def solution():
    """One of Robi's new year's resolutions is to start saving. He started to save $2 in January. This is followed by $4 in February and $8 in March. If he continues this saving pattern, how much will be his total savings after 6 months?"""
    savings = [2, 4, 8]
    for i in range(3, 6):
        savings.append(savings[i-1] * 2)
    total_savings = sum(savings)
    result = total_savings
    return result

print(solution())