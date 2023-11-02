def solution():
    # Define the total number of apartments
    total_apartments = 120

    # Calculate the number of apartments with at least one resident
    one_resident_apartments = int(total_apartments * 0.85)

    # Calculate the number of apartments with at least two residents
    two_resident_apartments = int(total_apartments * 0.6)

    # Calculate the number of apartments with only one resident
    only_one_resident_apartments = one_resident_apartments - two_resident_apartments

    result = only_one_resident_apartments
    return result

print(solution())