def solution():
    """Julian has 80 Facebook friends. 60% are boys and 40% are girls. Boyd has twice as many friends who are girls and has 100 friends total. What percentage of Boyd’s friends are boys?"""
    julian_friends = 80
    julian_boys = 0.6 * julian_friends
    julian_girls = 0.4 * julian_friends
    boyd_friends = 100
    boyd_girls = julian_girls * 2
    boyd_boys = boyd_friends - boyd_girls
    boy_percent = (boyd_boys / boyd_friends) * 100
    result = boy_percent
    return result

print(solution())