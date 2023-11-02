def solution():
    """Mary has a mystery book library. She started with 72 mystery books at the beginning of the year. She joined a book club that sent her 1 book each month of the year. She went to a bookstore halfway through the year and bought 5 more books, then bought 2 books at yard sales later. Her daughter gave her another book for her birthday, and her mother gave her a series of 4 books when Mary visited her. She donated 12 books she didn't want to read again to a charity shop and sold 3 to a used book store. How many books did she have at the end of the year?"""
    # Define the starting number of books
    starting_books = 72

    # Calculate the number of books received from the book club
    club_books = 12

    # Calculate the number of books bought at the bookstore and yard sales
    bought_books = 5 + 2

    # Calculate the number of books received as gifts
    gift_books = 1 + 4

    # Calculate the number of books donated and sold
    lost_books = 12 + 3

    # Calculate the total number of books at the end of the year
    total_books = starting_books + club_books + bought_books + gift_books - lost_books

    # Display the total number of books
    result = total_books
    return result

print(solution())