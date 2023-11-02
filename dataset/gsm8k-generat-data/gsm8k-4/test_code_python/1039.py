def solution():
    """In a block of flats, there are 120 apartments. 85% of them have at least 1 resident, while 60% of the apartments have at least two residents. How many apartments have only one resident?"""
    # Define the total number of apartments
    total_apartments = 120

    # Calculate the number of apartments with at least one resident
    at_least_one_resident = total_apartments * 0.85

    # Calculate the number of apartments with at least two residents
    at_least_two_residents = total_apartments * 0.6

    # Calculate the number of apartments with one resident
    one_resident = at_least_one_resident - at_least_two_residents

    # return the result
    result = one_resident
    return result

print(solution())