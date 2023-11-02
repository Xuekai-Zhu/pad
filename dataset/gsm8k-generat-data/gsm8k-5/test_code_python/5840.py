def solution():
    num_books = 10  # Phil has 10 books
    pages_per_book = 100  # Each book has 100 pages
    lost_books = 2  # 2 books are lost during the move

    # Calculate the total number of pages of books Phil has left
    total_pages = (num_books - lost_books) * pages_per_book
    result = total_pages
    return result

print(solution())