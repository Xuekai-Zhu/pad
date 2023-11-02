def solution():
    
    num_apartments = 120
    at_least_one_resident = 0.85
    at_least_two_residents = 0.6
    num_at_least_one_resident = num_apartments * at_least_one_resident
    num_at_least_two_residents = num_apartments * at_least_two_residents
    num_only_one_resident = num_at_least_one_resident - num_at_least_two_residents
    result = num_only_one_resident
    return result

print(solution())