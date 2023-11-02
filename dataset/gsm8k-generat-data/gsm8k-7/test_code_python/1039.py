def solution():
    total_apartments = 120
    percent_with_at_least_one_resident = 0.85
    percent_with_at_least_two_residents = 0.6

    # Calculate the number of apartments with at least one resident
    num_with_at_least_one_resident = total_apartments * percent_with_at_least_one_resident

    # Calculate the number of apartments with at least two residents
    num_with_at_least_two_residents = total_apartments * percent_with_at_least_two_residents

    # Calculate the number of apartments with only one resident
    num_with_only_one_resident = num_with_at_least_one_resident - num_with_at_least_two_residents

    result = num_with_only_one_resident
    return result

print(solution())