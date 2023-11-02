def solution():
    total_stickers = 750
    daniel_received = 250
    fred_received = daniel_received + 120

    # Calculate the total number of stickers shared with friends
    total_shared = daniel_received + fred_received

    # Calculate the number of stickers kept by Andrew
    stickers_kept = total_stickers - total_shared
    result = stickers_kept
    return result

print(solution())