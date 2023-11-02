def solution():
    """Julian has 80 Facebook friends. 60% are boys and 40% are girls. Boyd has twice as many friends who are girls and has 100 friends total. What percentage of Boyd’s friends are boys?"""
    julian_boys = 0.6 * 80
    julian_girls = 0.4 * 80
    boyd_girls = 2 * julian_girls
    boyd_total_friends = 100
    boyd_boys = boyd_total_friends - boyd_girls
    boyd_percent_boys = (boyd_boys / boyd_total_friends) * 100
    result = boyd_percent_boys
    return result

print(solution())