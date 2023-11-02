def solution():
    total_stickers = 750  # Andrew bought 750 stickers
    daniel_stickers = 250  # Daniel received 250 stickers
    fred_stickers = daniel_stickers + 120  # Fred received 120 more stickers than Daniel

    # Calculate the total number of stickers shared with Daniel and Fred
    shared_stickers = daniel_stickers + fred_stickers

    # Calculate the number of stickers Andrew kept
    remaining_stickers = total_stickers - shared_stickers
    result = remaining_stickers
    return result

print(solution())