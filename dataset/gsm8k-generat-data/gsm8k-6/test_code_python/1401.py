def solution():
    # Calculate the total number of towels used in one month
    total_towels = 3 + 6 + 3  # Kylie uses 3, daughters use 6, husband uses 3
    # Calculate the number of loads of laundry needed to clean all the towels
    loads_needed = total_towels // 4  # one load fits 4 towels
    if total_towels % 4 != 0:  # account for any remaining towels that won't fit in a full load
        loads_needed += 1
    result = loads_needed
    return result

print(solution())