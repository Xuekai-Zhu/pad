def solution():
    """Mary has a mystery book library. She started with 72 mystery books at the beginning of the year. She joined a book club that sent her 1 book each month of the year. She went to a bookstore halfway through the year and bought 5 more books, then bought 2 books at yard sales later. Her daughter gave her another book for her birthday, and her mother gave her a series of 4 books when Mary visited her. She donated 12 books she didn't want to read again to a charity shop and sold 3 to a used book store. How many books did she have at the end of the year?"""
    
    starting_books = 72
    book_club_books = 12
    bookstore_books = 5
    yard_sale_books = 2
    daughter_books = 1
    mother_books = 4
    donated_books = 12
    sold_books = 3
    total_books = starting_books + book_club_books + bookstore_books + yard_sale_books + daughter_books + mother_books - donated_books - sold_books
    result = total_books
    
    return result

print(solution())