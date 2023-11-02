def solution():
    total_stickers = 750
    daniel_stickers = 250
    fred_stickers = daniel_stickers + 120

    # Calculate the total number of stickers shared with Daniel and Fred
    shared_stickers = daniel_stickers + fred_stickers

    # Calculate the number of stickers that Andrew kept
    kept_stickers = total_stickers - shared_stickers
    result = kept_stickers
    return result

print(solution())