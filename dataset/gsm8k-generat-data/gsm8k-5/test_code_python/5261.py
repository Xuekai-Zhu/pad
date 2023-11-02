def solution():
    drinking_cooking_gallons = 100  # Jerry uses 100 gallons for drinking and cooking
    pool_volume = 10 * 10 * 6  # The pool measures 10 feet by 10 feet by 6 feet
    pool_gallons = pool_volume * 7.48  # Each cubic foot of water is equivalent to 7.48 gallons
    remaining_gallons = 1000 - drinking_cooking_gallons - pool_gallons  # Jerry can only use 1000 gallons in total
    shower_gallons = 20  # Jerry uses 20 gallons of water per shower

    # Calculate the number of showers Jerry can take in July
    num_showers = remaining_gallons // shower_gallons
    result = num_showers
    return result

print(solution())