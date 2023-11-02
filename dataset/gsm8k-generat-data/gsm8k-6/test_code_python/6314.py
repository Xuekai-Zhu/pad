def solution():
    # Calculate the number of ripe peaches after 5 days
    ripe_peaches = 4 + (2 * 5) - 3  # 4 ripe peaches initially, 2 more ripen every day, and 3 are eaten on day 3
    unripe_peaches = 18 - ripe_peaches  # calculate the number of unripe peaches remaining
    diff = ripe_peaches - unripe_peaches  # calculate the difference between ripe and unripe peaches
    result = diff
    return result

print(solution())