def solution():
    """Lauryn owns a computer company that employs men and women in different positions in the company. How many men does he employ if there are 20 fewer men than women and 180 people working for Lauryn?"""
    # Let's assume the number of men is m and the number of women is w
    # We know that m + w = 180 and m = w - 20
    # We can substitute the second equation into the first to get:
    # (w - 20) + w = 180
    # 2w - 20 = 180
    # 2w = 200
    # w = 100
    # Substituting w = 100 into m = w - 20, we get:
    # m = 100 - 20
    # m = 80
    
    # Therefore, Lauryn employs 80 men.
    result = 80
    return result

print(solution())