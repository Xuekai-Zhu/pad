def solution():
    Alicia_gumballs = 20
    Pedro_gumballs = Alicia_gumballs + (3 * Alicia_gumballs)
    total_gumballs = Alicia_gumballs + Pedro_gumballs
    gumballs_eaten = total_gumballs * 0.4
    gumballs_remaining = total_gumballs - gumballs_eaten
    result = gumballs_remaining
    return result

print(solution())