def solution():
    # Calculate the total number of candy necklaces
    total_candy_necklaces = 9 * 8

    # Subtract the number of remaining candy necklaces from the total to find the number taken by classmates
    candy_necklaces_taken = total_candy_necklaces - 40

    # Divide the number taken by classmates by the number of necklaces in each pack to find the packs opened
    packs_opened = candy_necklaces_taken / 8
    result = packs_opened
    return result

print(solution())