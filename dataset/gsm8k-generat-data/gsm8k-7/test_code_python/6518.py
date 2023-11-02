def solution():
    initial_pants = 50
    pairs_per_year = 4
    pants_per_pair = 2
    num_years = 5

    # Calculate the total number of pairs of pants Dani gets over 5 years
    total_pairs = pairs_per_year * num_years

    # Calculate the total number of pants he gets from those pairs
    total_pants_from_pairs = total_pairs * pants_per_pair

    # Add the initial pants he had to the total pants he gets from the pairs
    total_pants = initial_pants + total_pants_from_pairs
    result = total_pants
    return result

print(solution())