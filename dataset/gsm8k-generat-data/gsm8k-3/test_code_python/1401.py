def solution():
    """In one month in the Smith house, Kylie uses 3 bath towels, her 2 daughters use a total of 6 bath towels, and her husband uses a total of 3 bath towels. If the washing machine can fit 4 bath towels for one load of laundry, how many loads of laundry will the Smiths need to do to clean all of their used towels?"""
    # Define the number of towels used by each family member
    KYLIE_TOWELS = 3
    DAUGHTER_TOWELS = 6 / 2 # Each daughter uses half
    HUSBAND_TOWELS = 3

    # Calculate the total number of towels used
    total_towels = KYLIE_TOWELS + DAUGHTER_TOWELS + HUSBAND_TOWELS

    # Calculate the number of loads of laundry needed
    loads_needed = total_towels / 4

    # Round up to the nearest whole number
    loads_needed = math.ceil(loads_needed)

    # Display the number of loads needed
    result = loads_needed
    return result

print(solution())