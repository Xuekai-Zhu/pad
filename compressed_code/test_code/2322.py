def solution():
    
    total_books = 120
    novels = int(total_books * 0.65)
    graphic_novels = 18
    comic_books = total_books - novels - graphic_novels
    comic_percentage = (comic_books / total_books) * 100
    result = comic_percentage
    return result

print(solution())