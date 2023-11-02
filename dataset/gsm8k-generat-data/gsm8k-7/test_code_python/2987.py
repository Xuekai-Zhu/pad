def solution():
    total_books = 120
    novels_percent = 65
    graphic_novels = 18
    
    # Calculate the number of novels
    novels = total_books * novels_percent / 100
    
    # Calculate the number of comic books
    comic_books = total_books - novels - graphic_novels
    
    # Calculate the percentage of comic books
    comic_books_percent = comic_books / total_books * 100

    result = comic_books_percent
    return result

print(solution())