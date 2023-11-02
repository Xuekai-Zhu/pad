def solution():
    """Camden went swimming 16 times in March and Susannah went 24 times. If the number of times they went throughout the month was divided equally among 4 weeks, how many more times a week did Susannah swim than Camden?"""
    camden_swims = 16
    susannah_swims = 24
    total_swims = camden_swims + susannah_swims
    swims_per_week = total_swims / 4
    camden_per_week = camden_swims / 4
    susannah_per_week = susannah_swims / 4
    difference = susannah_per_week - camden_per_week
    result = difference
    return result

print(solution())