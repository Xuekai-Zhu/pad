def solution():
    # Calculate the total number of rose petals needed to make 20 12-ounce bottles of perfume
    total_petals_needed = 320 * 12 * 20

    # Calculate the total number of roses needed to get the required number of petals
    roses_needed = total_petals_needed / 8

    # Calculate the number of bushes needed to get the required number of roses
    bushes_needed = roses_needed / 12

    result = bushes_needed
    return result

print(solution())