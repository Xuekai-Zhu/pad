def solution():
    """Adam has just bought some new books so he has decided to clean up his bookcase. After he adds his new books to his bookshelf he realizes that he has bought enough books to finish completely filling his bookcase with 2 books left over. Before his shopping trip, Adam had 56 books in his bookcase. If his bookcase has 4 shelves and averages 20 books per shelf, how many books did Adam buy on his shopping trip?"""
    total_books_before = 56
    shelves = 4
    books_per_shelf = 20
    total_books_after = shelves * books_per_shelf
    books_left_over = total_books_after - (total_books_before + 2)
    books_bought = books_left_over
    result = books_bought
    return result

print(solution())