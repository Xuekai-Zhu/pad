def solution():
    # Calculate the total number of water bottles
    total_bottles = 4 * 12  # four dozen water bottles

    # Calculate the number of bottles taken by the players
    bottles_taken = 11 * 2 + 11 * 1  # 11 players each take 2 bottles in the first break and 1 more bottle at the end of the game

    # Calculate the number of bottles remaining
    bottles_remaining = total_bottles - bottles_taken
    result = bottles_remaining
    return result

print(solution())