def solution():
    total_pages = 95  # total number of pages in the book
    num_chapters = 5  # number of chapters in the book

    # Calculate the difference in pages between each chapter
    diff_pages = 3

    # Calculate the number of pages in the first chapter
    first_chapter_pages = (total_pages - diff_pages*(num_chapters-1)) // (num_chapters*(num_chapters+1)//2)

    result = first_chapter_pages
    return result

print(solution())