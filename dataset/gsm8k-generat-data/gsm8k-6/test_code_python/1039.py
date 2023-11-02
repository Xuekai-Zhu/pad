def solution():
    total_apartments = 120
    apartments_with_single_resident = total_apartments * 0.85  # 85% of apartments have at least 1 resident
    apartments_with_two_or_more_residents = total_apartments * 0.6  # 60% of apartments have at least 2 residents
    apartments_with_only_one_resident = apartments_with_single_resident - apartments_with_two_or_more_residents
    result = apartments_with_only_one_resident
    return result

print(solution())