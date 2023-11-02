def solution():
    # Calculate the number of cans collected by Diego
    martha_cans = 90
    diego_cans = (1/2) * martha_cans + 10

    # Calculate the number of cans they still need to collect
    total_cans = 150
    cans_left = total_cans - (martha_cans + diego_cans)
    result = cans_left
    return result

print(solution())