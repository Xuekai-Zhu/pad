def solution():
    """In one month in the Smith house, Kylie uses 3 bath towels, her 2 daughters use a total of 6 bath towels, and her husband uses a total of 3 bath towels. If the washing machine can fit 4 bath towels for one load of laundry, how many loads of laundry will the Smiths need to do to clean all of their used towels?"""
    # Define the number of towels used by each family member
    kylie_towels = 3
    daughter_towels = 6
    husband_towels = 3

    # Calculate the total number of towels used
    total_towels = kylie_towels + daughter_towels + husband_towels

    # Calculate the number of loads of laundry needed
    loads_of_laundry = total_towels / 4

    # Round up to the nearest whole number of loads
    loads_of_laundry = math.ceil(loads_of_laundry)

    # return the result
    result = loads_of_laundry
    return result

print(solution())