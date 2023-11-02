def solution():
    """Julie, Micah, and Mitchell sold 32 glasses of lemonade at their lemonade stand. Julie sold 14 glasses and the boys sold an equal number of glasses. How many more glasses did Julie sell than Micah?"""
    total_sales = 32
    julie_sales = 14
    boy_sales = (total_sales - julie_sales) / 2
    micah_sales = boy_sales
    difference = julie_sales - micah_sales
    result = difference
    return result

print(solution())