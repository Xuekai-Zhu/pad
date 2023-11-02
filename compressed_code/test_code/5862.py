def solution():
    
    gumballs_given_todd = 4
    gumballs_given_alisha = gumballs_given_todd * 2
    gumballs_given_bobby = (4 * gumballs_given_alisha) - 5
    total_given_away = gumballs_given_todd + gumballs_given_alisha + gumballs_given_bobby
    total_gumballs = total_given_away + 6
    result = total_gumballs
    return result

print(solution())