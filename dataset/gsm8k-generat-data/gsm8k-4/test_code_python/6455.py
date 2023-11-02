def solution():
    """Adam has just bought some new books so he has decided to clean up his bookcase. After he adds his new books to his bookshelf he realizes that he has bought enough books to finish completely filling his bookcase with 2 books left over. Before his shopping trip, Adam had 56 books in his bookcase. If his bookcase has 4 shelves and averages 20 books per shelf, how many books did Adam buy on his shopping trip?"""
    
    # Define the number of shelves and average number of books per shelf
    shelves = 4
    average_books_per_shelf = 20
    
    # Calculate the maximum number of books that can fit in the bookcase
    max_books = shelves * average_books_per_shelf
    
    # Calculate the number of books that Adam had before his shopping trip
    initial_books = 56
    
    # Calculate the number of books Adam bought on his shopping trip
    bought_books = max_books - initial_books - 2
    
    # Return the result
    result = bought_books
    return result

print(solution())