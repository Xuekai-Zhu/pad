def solution():
    
    total_stickers = 750
    daniel_stickers = 250
    fred_stickers = daniel_stickers + 120
    distributed_stickers = daniel_stickers + fred_stickers
    remaining_stickers = total_stickers - distributed_stickers
    result = remaining_stickers
    return result

print(solution())