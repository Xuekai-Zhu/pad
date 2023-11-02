def solution():
    
    total_books = 120
    percent_novels = 65
    graphic_novels = 18
    novels = total_books * (percent_novels / 100)
    comic_books = total_books - novels - graphic_novels
    percent_comic_books = (comic_books / total_books) * 100
    result = percent_comic_books
    return result

print(solution())