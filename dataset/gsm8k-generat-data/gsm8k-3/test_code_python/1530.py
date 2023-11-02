def solution():
    """Miles is going to spend 1/6 of a day reading. He will read comic books, graphic novels, and novels. He reads 21 pages an hour when he reads novels, 30 pages an hour when he reads graphic novels, and 45 pages an hour when he reads comic books. If he reads each for 1/3 of his time, how many pages does he read?"""
    # Define the number of hours Miles will spend reading
    HOURS_READING = 4

    # Define the number of pages Miles reads per hour for each type of book
    NOVEL_PAGES_PER_HOUR = 21
    GRAPHIC_NOVEL_PAGES_PER_HOUR = 30
    COMIC_BOOK_PAGES_PER_HOUR = 45

    # Calculate the number of pages Miles reads for each type of book
    novel_pages = NOVEL_PAGES_PER_HOUR * (HOURS_READING / 3)
    graphic_novel_pages = GRAPHIC_NOVEL_PAGES_PER_HOUR * (HOURS_READING / 3)
    comic_book_pages = COMIC_BOOK_PAGES_PER_HOUR * (HOURS_READING / 3)

    # Calculate the total number of pages Miles reads
    total_pages = novel_pages + graphic_novel_pages + comic_book_pages

    # Display the total number of pages
    result = total_pages
    return result

print(solution())