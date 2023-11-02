def solution():
    """There were 18 stamps in Parker’s scrapbook. If Addie put one fourth of her 72 stamps in Parker’s scrapbook, how many stamps does he have now?"""
    parker_stamps = 18
    addie_stamps = 72
    parker_stamps += addie_stamps / 4
    result = parker_stamps
    return result

print(solution())