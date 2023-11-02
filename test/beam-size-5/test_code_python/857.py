def solution():
    
    claire_badges_per_month = 1
    amber_badges_per_month = claire_badges_per_month * 2
    wendy_badges_per_month = 3 * claire_badges_per_month
    amber_badges_per_year = amber_badges_per_month * 12
    wendy_badges_per_year = wendy_badges_per_year * 12
    difference = wendy_badges_per_year - amber_badges_per_year
    result = difference
    return result

print(solution())