def solution():
    """Adam has just bought some new books so he has decided to clean up his bookcase. After he adds his new books to his bookshelf he realizes that he has bought enough books to finish completely filling his bookcase with 2 books left over. Before his shopping trip, Adam had 56 books in his bookcase. If his bookcase has 4 shelves and averages 20 books per shelf, how many books did Adam buy on his shopping trip?"""
    # Calculate the total capacity of the bookcase
    bookcase_capacity = 4 * 20

    # Calculate the number of books Adam had before his shopping trip
    initial_books = 56

    # Determine how many books are needed to fill the bookcase
    books_needed = bookcase_capacity - initial_books + 2

    # Display the number of books Adam bought
    result = books_needed
    return result

print(solution())