def solution():
    """Andrew bought 750 stickers. He shared some of his stickers with his friends, Daniel and Fred. Daniel received 250 stickers,
     while Fred received 120 more stickers than Daniel. He kept the remaining stickers. How many stickers did Andrew keep?"""
    total_stickers = 750
    daniel_stickers = 250
    fred_stickers = daniel_stickers + 120
    distributed_stickers = daniel_stickers + fred_stickers
    remaining_stickers = total_stickers - distributed_stickers
    result = remaining_stickers
    return result

print(solution())