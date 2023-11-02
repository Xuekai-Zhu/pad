def solution():
    """Matias is a salesman in a bookstore. He sold 7 books on Tuesday and three times as many on Wednesday. If the sales from Wednesday were tripled on Thursday, how many books did Matias sell during these three days combined?"""
    # Calculate the number of books sold on Wednesday
    wednesday_sales = 7 * 3

    # Calculate the number of books sold on Thursday
    thursday_sales = wednesday_sales * 3

    # Calculate the total number of books sold
    total_sales = 7 + wednesday_sales + thursday_sales

    # Display the total number of books sold
    result = total_sales
    return result

print(solution())