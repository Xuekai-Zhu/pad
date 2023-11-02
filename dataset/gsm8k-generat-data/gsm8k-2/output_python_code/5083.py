def solution():
    """On a tough week, Haji's mother sells goods worth $800, which is half the amount she sells on a good week. What's the total amount of money she makes if she has 5 good weeks and 3 tough weeks?"""
    good_week_sales = 2 * 800
    tough_week_sales = 800
    total_sales = (good_week_sales * 5) + (tough_week_sales * 3)
    result = total_sales
    return result

print(solution())