def solution():
    # Calculate the total number of beach towels used in one day
    towels_per_day = 3 * 4

    # Calculate the total number of towels used over the 7-day vacation
    total_towels = towels_per_day * 7

    # Calculate the number of loads needed to wash all the towels
    loads_needed = total_towels // 14

    if total_towels % 14 != 0:
        loads_needed += 1

    result = loads_needed
    return result

print(solution())