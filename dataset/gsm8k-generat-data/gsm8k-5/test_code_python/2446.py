def solution():
    # Calculate the total number of skips for Bob and Jim
    bob_skips = 12 * 10  # Bob can skip a rock 12 times, and he skips 10 rocks
    jim_skips = 15 * 10  # Jim can skip a rock 15 times, and he skips 10 rocks

    # Calculate the total number of skips for both of them
    total_skips = bob_skips + jim_skips
    result = total_skips
    return result

print(solution())