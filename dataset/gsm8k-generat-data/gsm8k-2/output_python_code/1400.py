def solution():
    """In one month in the Smith house, Kylie uses 3 bath towels, her 2 daughters use a total of 6 bath towels, and her husband uses a total of 3 bath towels. If the washing machine can fit 4 bath towels for one load of laundry, how many loads of laundry will the Smiths need to do to clean all of their used towels?"""
    kylie_towels = 3
    daughters_towels = 6
    husband_towels = 3
    total_towels = kylie_towels + daughters_towels + husband_towels
    loads = total_towels // 4
    if total_towels % 4 != 0:
        loads += 1
    result = loads
    return result

print(solution())