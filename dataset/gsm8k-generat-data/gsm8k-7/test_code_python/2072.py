def solution():
    remaining_popsicles = 6

    # Iterate through each melted popsicle and double the rate of melting
    for i in range(remaining_popsicles - 1):
        remaining_popsicles /= 2

    # Calculate the ratio of melting rates between the last popsicle and the first popsicle
    ratio = remaining_popsicles / 1

    result = ratio
    return result

print(solution())