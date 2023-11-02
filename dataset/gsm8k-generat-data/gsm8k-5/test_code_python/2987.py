def solution():
    total_books = 120

    # Calculate the number of novels
    novels = total_books * 0.65

    # Calculate the number of graphic novels
    graphic_novels = 18

    # Calculate the number of comic books
    comic_books = total_books - novels - graphic_novels

    # Calculate the percentage of comic books
    percentage_comic_books = (comic_books / total_books) * 100
    result = percentage_comic_books
    return result

print(solution())