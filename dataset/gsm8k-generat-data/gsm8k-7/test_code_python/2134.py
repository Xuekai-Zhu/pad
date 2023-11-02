def solution():
    martha_cans = 90
    diego_cans = (0.5 * martha_cans) + 10
    total_cans = 150

    # Calculate the number of cans they have already collected
    collected_cans = martha_cans + diego_cans

    # Calculate the number of cans they still need to collect
    remaining_cans = total_cans - collected_cans
    result = remaining_cans
    return result

print(solution())