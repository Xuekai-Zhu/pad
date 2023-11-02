def solution():
    """Ali had a stock of 800 books in his Room. He sold 60 on Monday, 10 on Tuesday, 20 on Wednesday, 44 on Thursday and 66 on Friday. How many books were not sold?"""
    initial_stock = 800
    books_sold = 60 + 10 + 20 + 44 + 66
    books_not_sold = initial_stock - books_sold
    result = books_not_sold
    return result

print(solution())