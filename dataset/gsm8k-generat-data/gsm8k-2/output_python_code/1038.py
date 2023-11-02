def solution():
    """In a block of flats, there are 120 apartments. 85% of them have at least 1 resident, while 60% of the apartments have at least two residents. How many apartments have only one resident?"""
    total_apartments = 120
    at_least_one_resident = 0.85 * total_apartments
    at_least_two_residents = 0.6 * total_apartments
    only_one_resident = at_least_one_resident - at_least_two_residents
    result = only_one_resident
    return result

print(solution())