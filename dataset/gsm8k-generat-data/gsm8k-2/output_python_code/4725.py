def solution():
    """Matias is a salesman in a bookstore. He sold 7 books on Tuesday and three times as many on Wednesday. If the sales from Wednesday were tripled on Thursday, how many books did Matias sell during these three days combined?"""
    tuesday_sales = 7
    wednesday_sales = 3 * tuesday_sales
    thursday_sales = 3 * wednesday_sales
    total_sales = tuesday_sales + wednesday_sales + thursday_sales
    result = total_sales
    return result

print(solution())