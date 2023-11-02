def solution():
    karl_stickers = 25  # Karl has 25 stickers
    ryan_stickers = karl_stickers + 20  # Ryan has 20 more stickers than Karl
    ben_stickers = ryan_stickers - 10  # Ben has 10 fewer stickers than Ryan

    # Calculate the total number of stickers
    total_stickers = karl_stickers + ryan_stickers + ben_stickers
    result = total_stickers
    return result

print(solution())