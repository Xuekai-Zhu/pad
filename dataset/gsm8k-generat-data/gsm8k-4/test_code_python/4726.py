def solution():
    """Matias is a salesman in a bookstore. He sold 7 books on Tuesday and three times as many on Wednesday. If the sales from Wednesday were tripled on Thursday, how many books did Matias sell during these three days combined?"""
    # Define the number of books sold on Tuesday
    tuesday_sales = 7

    # Define the number of books sold on Wednesday (three times as many as Tuesday)
    wednesday_sales = 3 * tuesday_sales

    # Define the number of books sold on Thursday (triple the sales on Wednesday)
    thursday_sales = 3 * wednesday_sales

    # Calculate the total number of books sold during the three days
    total_sales = tuesday_sales + wednesday_sales + thursday_sales

    # return the result
    result = total_sales
    return result

print(solution())