def solution():
    """Alden had 50 nephews ten years ago. This is half the number of nephews Alden has now. If Vihaan has 60 more nephews than Alden now, how many nephews do the two have altogether?"""
    aldens_nephews_ten_years_ago = 50
    aldens_current_nephews = aldens_nephews_ten_years_ago * 2
    vihaans_nephews = aldens_current_nephews + 60
    total_nephews = aldens_current_nephews + vihaans_nephews
    result = total_nephews
    return result

print(solution())