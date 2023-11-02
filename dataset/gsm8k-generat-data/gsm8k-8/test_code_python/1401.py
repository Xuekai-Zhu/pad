def solution():
    # Calculate the total number of bath towels used
    total_towels_used = 3 + 6 + 3

    # Calculate the number of loads needed for all the towels
    loads_needed = total_towels_used / 4

    # Round up to ensure enough loads are done
    loads_rounded = math.ceil(loads_needed)

    result = loads_rounded
    return result

print(solution())