def solution():
    """Every Halloween one house in the neighborhood gives out toothbrushes instead of candy, so it always gets egged and covered in toilet paper. If the owner spends 15 seconds cleaning up each egg and 30 minutes cleaning up each roll of toilet paper, how long (in minutes) will they have to spend cleaning up 60 eggs and 7 rolls of toilet paper?"""
    eggs = 60
    toilet_paper = 7
    egg_cleanup_time = eggs * 15/60
    toilet_paper_cleanup_time = toilet_paper * 30
    total_cleanup_time = egg_cleanup_time + toilet_paper_cleanup_time
    result = total_cleanup_time

    return result

print(solution())