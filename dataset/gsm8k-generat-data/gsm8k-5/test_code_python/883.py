def solution():
    bolts_per_box = 11  # Each box of bolts contains 11 bolts
    nuts_per_box = 15  # Each box of nuts contains 15 nuts
    total_bolts = 7 * bolts_per_box  # Total number of bolts purchased
    total_nuts = 3 * nuts_per_box  # Total number of nuts purchased
    bolts_leftover = 3  # Number of bolts left over after completing the project
    nuts_leftover = 6  # Number of nuts left over after completing the project
    bolts_used = total_bolts - bolts_leftover  # Number of bolts used in the project
    nuts_used = total_nuts - nuts_leftover  # Number of nuts used in the project
    result = (bolts_used, nuts_used)
    return result

print(solution())