def solution():
    # Calculate the number of tiles painted by each person in 1 minute
    tiles_painted_Don = 3
    tiles_painted_Ken = 5  # 2 more than Don
    tiles_painted_Laura = 10  # twice as many as Ken
    tiles_painted_Kim = 7  # 3 fewer than Laura

    # Calculate the total number of tiles painted by all four people in 15 minutes
    total_tiles_painted = 15*(tiles_painted_Don + tiles_painted_Ken + tiles_painted_Laura + tiles_painted_Kim)
    result = total_tiles_painted
    return result

print(solution())