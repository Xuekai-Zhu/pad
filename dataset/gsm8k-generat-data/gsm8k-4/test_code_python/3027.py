def solution():
    """Mary has a mystery book library. She started with 72 mystery books at the beginning of the year. 
    She joined a book club that sent her 1 book each month of the year. She went to a bookstore halfway 
    through the year and bought 5 more books, then bought 2 books at yard sales later. Her daughter 
    gave her another book for her birthday, and her mother gave her a series of 4 books when Mary visited her. 
    She donated 12 books she didn't want to read again to a charity shop and sold 3 to a used book store. 
    How many books did she have at the end of the year?"""
    # Define the initial number of books
    books = 72

    # Joining a book club, a book was sent each month, total of 12 books
    books += 12

    # Bookstore purchase
    books += 5

    # Purchase at yard sale
    books += 2

    # Daughter's gift
    books += 1

    # Mother's gift
    books += 4

    # Charity shop donation
    books -= 12

    # Sold to a used bookstore
    books -= 3

    # Return the final number of books
    result = books
    return result

print(solution())