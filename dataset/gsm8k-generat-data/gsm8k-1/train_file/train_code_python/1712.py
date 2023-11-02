def solution():
    """The hobby store normally sells 21,122 trading cards per month. In June, the hobby store sold 3,922 more trading cards than normal.
    If the hobby store sold the regular number of trading cards in July, how many trading cards did the hobby store sell in June and July combined?"""
    normal_sales = 21122
    june_sales = normal_sales + 3922
    july_sales = normal_sales
    total_sales = june_sales + july_sales
    result = total_sales
    return result

print(solution())