def solution():
    alicia_gumballs = 20

    pedro_gumballs = alicia_gumballs + (3 * alicia_gumballs)

    total_gumballs = alicia_gumballs + pedro_gumballs

    num_gumballs_eaten = total_gumballs * 0.4

    remaining_gumballs = total_gumballs - num_gumballs_eaten
    result = remaining_gumballs
    return result

print(solution())