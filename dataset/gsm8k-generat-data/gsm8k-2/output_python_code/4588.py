def solution():
    """Every Halloween one house in the neighborhood gives out toothbrushes instead of candy, so it always gets egged and covered in toilet paper. If the owner spends 15 seconds cleaning up each egg and 30 minutes cleaning up each roll of toilet paper, how long (in minutes) will they have to spend cleaning up 60 eggs and 7 rolls of toilet paper?"""
    egg_clean_time = 15 / 60 # in minutes
    tp_clean_time = 30 # in minutes
    total_time = egg_clean_time * 60 * 60 * 60 + tp_clean_time * 7
    result = total_time
    return result

print(solution())