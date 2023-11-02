def solution():
    total_apartments = 120  # There are 120 apartments in the block

    # Calculate the number of apartments with at least 1 resident
    apartments_with_at_least_one_resident = total_apartments * 0.85

    # Calculate the number of apartments with at least 2 residents
    apartments_with_at_least_two_residents = total_apartments * 0.6

    # Calculate the number of apartments with only 1 resident
    apartments_with_one_resident = apartments_with_at_least_one_resident - apartments_with_at_least_two_residents

    result = apartments_with_one_resident
    return result

print(solution())