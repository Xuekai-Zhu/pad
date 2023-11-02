def solution():
    """Alicia has 20 gumballs. Pedro has that many gumballs plus an additional number of gumballs equal to three times the number Alicia has. They put their gumballs in a bowl, and later Pedro takes out 40% of the gumballs to eat. How many gumballs are remaining in the bowl?"""
    alicia_gumballs = 20
    pedro_gumballs = alicia_gumballs + 3 * alicia_gumballs
    total_gumballs = alicia_gumballs + pedro_gumballs
    eaten_gumballs = 0.4 * total_gumballs
    remaining_gumballs = total_gumballs - eaten_gumballs
    result = remaining_gumballs
    return result

print(solution())