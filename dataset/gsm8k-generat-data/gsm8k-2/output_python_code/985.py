def solution():
    """Camden went swimming 16 times in March and Susannah went 24 times. If the number of times they went throughout the month was divided equally among 4 weeks, how many more times a week did Susannah swim than Camden?"""
    camden_swim = 16
    susannah_swim = 24
    total_swim = camden_swim + susannah_swim
    swim_per_week = total_swim / 4
    susannah_per_week = susannah_swim / 4
    camden_per_week = camden_swim / 4
    difference = susannah_per_week - camden_per_week
    result = difference
    return result

print(solution())