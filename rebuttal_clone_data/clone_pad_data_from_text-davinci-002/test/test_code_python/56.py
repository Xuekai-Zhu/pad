def solution():
    
    gumballs_given_to_todd = 4
    gumballs_given_to_alisha = 2 * gumballs_given_to_todd
    gumballs_given_to_bobby = (4 * gumballs_given_to_alisha) - 5
    gumballs_remaining = 6
    total_gumballs = gumballs_given_to_todd + gumballs_given_to_alisha + gumballs_given_to_bobby + gumballs_remaining
    result = total_gumballs
    return result

print(solution())