def solution():
    """In one month in the Smith house, Kylie uses 3 bath towels, her 2 daughters use a total of 6 bath towels, and her husband uses a total of 3 bath towels. If the washing machine can fit 4 bath towels for one load of laundry, how many loads of laundry will the Smiths need to do to clean all of their used towels?"""
    total_towels = 3 + 6 + 3
    towels_per_load = 4
    loads_of_laundry = total_towels // towels_per_load + (total_towels % towels_per_load > 0)
    result = loads_of_laundry
    return result

print(solution())