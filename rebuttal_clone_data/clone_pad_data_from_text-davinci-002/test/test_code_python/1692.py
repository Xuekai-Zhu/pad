def solution():
    total_books = 120
    novels = total_books * 0.65
    graphic_novels = 18
    comic_books = total_books - novels - graphic_novels
    percent_comic_books = (comic_books / total_books) * 100
    result = percent_comic_books
    
    return result

print(solution())