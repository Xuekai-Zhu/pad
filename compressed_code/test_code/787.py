def solution():
    
    total_apartments = 120
    at_least_one_resident = 0.85 * total_apartments
    at_least_two_residents = 0.6 * total_apartments
    only_one_resident = at_least_one_resident - at_least_two_residents
    result = only_one_resident
    return result

print(solution())