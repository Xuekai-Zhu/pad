def solution():
    # Calculate the number of novels
    num_novels = 0.65 * 120

    # Calculate the number of comic books
    num_comic_books = 120 - num_novels - 18

    # Calculate the percentage of comic books
    comic_percent = (num_comic_books / 120) * 100

    result = comic_percent
    return result

print(solution())