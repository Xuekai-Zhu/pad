def solution():
    pairs_per_year = 4 # Dani gets 4 pairs of pants each year
    pants_per_pair = 2 # Each pair contains 2 pants
    initial_pants = 50 # Dani initially has 50 pants
    years = 5 # Dani wants to know how many pants he will have in 5 years

    # Calculate the total number of pairs of pants Dani will receive in 5 years
    total_pairs = pairs_per_year * years

    # Calculate the total number of pants Dani will receive in 5 years
    total_pants = total_pairs * pants_per_pair

    # Calculate the total number of pants Dani will have in 5 years
    total_pants += initial_pants

    result = total_pants
    return result

print(solution())