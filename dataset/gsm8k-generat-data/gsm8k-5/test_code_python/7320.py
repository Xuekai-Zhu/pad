def solution():
    alicia_gumballs = 20
    pedro_gumballs = alicia_gumballs + (3 * alicia_gumballs)
    total_gumballs = alicia_gumballs + pedro_gumballs
    eaten_gumballs = 0.4 * total_gumballs
    remaining_gumballs = total_gumballs - eaten_gumballs
    result = remaining_gumballs
    return result

print(solution())