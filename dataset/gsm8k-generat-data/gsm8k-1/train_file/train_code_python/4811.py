def solution():
    """On Monday, a restaurant sells forty dinners. On Tuesday, it sells 40 more dinners than it did Monday. On Wednesday, it sells half the amount of dinners it sold on Tuesday. On Thursday they changed their recipe, and then sold 3 more dinners than they did on Wednesday. How many dinners were sold in those 4 days?"""
    monday = 40
    tuesday = monday + 40
    wednesday = tuesday / 2
    thursday = wednesday + 3
    total_dinners = monday + tuesday + wednesday + thursday
    result = total_dinners
    return result

print(solution())