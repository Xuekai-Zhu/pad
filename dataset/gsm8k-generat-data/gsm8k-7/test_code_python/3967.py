def solution():
    num_roses = 2 * 12  # two dozen roses
    num_chocolates = 1

    # Danielle traded the chocolates for another dozen roses
    num_roses += 1 * 12

    # Half of the roses wilted overnight
    num_roses /= 2

    # Half of the remaining roses wilted on the second day
    num_roses /= 2

    # Calculate the number of unwilted roses remaining
    num_unwilted_roses = num_roses
    result = num_unwilted_roses
    return result

print(solution())