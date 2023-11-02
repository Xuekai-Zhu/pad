def solution():
    # Calculate the total number of hats Miggy's mom brought home
    total_hats = 3 * 15  # each bag has 15 hats

    # Calculate the number of unused hats
    unused_hats = total_hats - (25 + 5)  # 25 hats were used during the party and 5 hats were torn off
    result = unused_hats
    return result

print(solution())