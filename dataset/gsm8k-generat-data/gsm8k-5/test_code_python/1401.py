def solution():
    kylie_towels = 3  # Kylie uses 3 bath towels in one month
    daughters_towels = 6  # Kylie's daughters use a total of 6 bath towels in one month
    husband_towels = 3  # Kylie's husband uses a total of 3 bath towels in one month
    total_towels = kylie_towels + daughters_towels + husband_towels  # Calculate the total number of bath towels used in one month

    # Calculate the number of loads of laundry needed to clean all the used towels
    loads_of_laundry = total_towels // 4  # Round down to the nearest whole number, since 4 towels fit in one load

    if total_towels % 4 != 0:
        loads_of_laundry += 1  # Add one more load if there are any leftover towels

    result = loads_of_laundry
    return result

print(solution())