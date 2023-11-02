def solution():
    # Calculate the total number of stickers shared with Daniel and Fred
    shared_stickers = 250 + (250+120)  # Daniel received 250 stickers, Fred received 120 more stickers than Daniel

    # Calculate the number of stickers Andrew kept
    remaining_stickers = 750 - shared_stickers
    result = remaining_stickers
    return result

print(solution())