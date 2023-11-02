def solution():
    # Calculate the total number of candy necklaces
    total_candy_necklaces = 9 * 8  # 9 packs with 8 candy necklaces in each

    # Calculate the number of candy necklaces taken by classmates
    candy_necklaces_taken = total_candy_necklaces - 40

    # Calculate the number of packs opened
    packs_opened = (total_candy_necklaces - candy_necklaces_taken) / 8

    result = packs_opened
    return result

print(solution())