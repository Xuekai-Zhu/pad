def solution():
    """Alicia has 20 gumballs. Pedro has that many gumballs plus an additional number of gumballs equal to three times the number Alicia has.
    They put their gumballs in a bowl, and later Pedro takes out 40% of the gumballs to eat. How many gumballs are remaining in the bowl?"""
    alicia_gumballs = 20
    pedro_gumballs = 20 + (3 * alicia_gumballs)
    total_gumballs = alicia_gumballs + pedro_gumballs
    gumballs_eaten = round(total_gumballs * 0.4) # round to nearest integer
    gumballs_remaining = total_gumballs - gumballs_eaten
    result = gumballs_remaining
    return result

print(solution())