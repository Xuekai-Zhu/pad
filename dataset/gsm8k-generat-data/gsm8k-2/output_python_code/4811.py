def solution():
    """On Monday, a restaurant sells forty dinners. On Tuesday, it sells 40 more dinners than it did Monday. On Wednesday, it sells half the amount of dinners it sold on Tuesday. On Thursday they changed their recipe, and then sold 3 more dinners than they did on Wednesday. How many dinners were sold in those 4 days?"""
    monday_sales = 40
    tuesday_sales = monday_sales + 40
    wednesday_sales = tuesday_sales / 2
    thursday_sales = wednesday_sales + 3
    total_sales = monday_sales + tuesday_sales + wednesday_sales + thursday_sales
    result = total_sales
    return result

print(solution())