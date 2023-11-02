def solution():
    # Calculate the total number of pants Dani will have in 5 years
    new_pants_each_year = 4*2  # Dani gets 4 pairs of 2 pants each year
    total_new_pants_in_5_years = new_pants_each_year * 5  # Dani gets new pants each year for 5 years
    total_pants_in_5_years = 50 + total_new_pants_in_5_years  # Dani initially had 50 pants
    result = total_pants_in_5_years
    return result

print(solution())