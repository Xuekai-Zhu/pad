def solution():
    """Alden had 50 nephews ten years ago. This is half the number of nephews Alden has now. If Vihaan has 60 more nephews than Alden now, how many nephews do the two have altogether?"""
    aldens_nephews_now = 50 * 2
    vihaans_nephews_now = aldens_nephews_now + 60
    total_nephews = aldens_nephews_now + vihaans_nephews_now
    result = total_nephews
    return result

print(solution())