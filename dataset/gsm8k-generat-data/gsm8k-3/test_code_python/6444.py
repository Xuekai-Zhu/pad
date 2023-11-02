def solution():
    """Ali had a stock of 800 books in his Room. He sold 60 on Monday, 10 on Tuesday, 20 on Wednesday, 44 on Thursday and 66 on Friday. How many books were not sold?"""
    # Define the initial stock of books
    initial_stock = 800

    # Define the number of books sold each day
    monday_sales = 60
    tuesday_sales = 10
    wednesday_sales = 20
    thursday_sales = 44
    friday_sales = 66

    # Calculate the total number of books sold
    total_sales = monday_sales + tuesday_sales + wednesday_sales + thursday_sales + friday_sales

    # Calculate the number of books not sold
    books_not_sold = initial_stock - total_sales

    # Display the number of books not sold
    result = books_not_sold
    return result

print(solution())