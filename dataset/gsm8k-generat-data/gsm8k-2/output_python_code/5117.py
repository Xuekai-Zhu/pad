def solution():
    """On the first day of the garden center sale, 14 marigolds were sold. The next day 25 more marigolds were sold. On the third day the center sold two times the number of marigolds it did on the day before. How many marigolds were sold during the sale?"""
    day1_sales = 14
    day2_sales = day1_sales + 25
    day3_sales = 2 * day2_sales
    total_sales = day1_sales + day2_sales + day3_sales
    result = total_sales
    return result

print(solution())