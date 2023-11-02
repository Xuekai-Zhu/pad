def solution():
    
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