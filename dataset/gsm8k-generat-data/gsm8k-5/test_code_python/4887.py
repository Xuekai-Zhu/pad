def solution():
    total_stickers = 135  # Oliver had 135 stickers
    used_stickers = total_stickers * (1/3)  # Oliver used 1/3 of his stickers
    remaining_stickers = total_stickers - used_stickers  # Oliver has this many stickers left
    given_away_stickers = remaining_stickers * (2/5)  # Oliver gives away 2/5 of his remaining stickers
    kept_stickers = remaining_stickers - given_away_stickers  # Oliver keeps the rest of his stickers
    result = kept_stickers
    return result

print(solution())