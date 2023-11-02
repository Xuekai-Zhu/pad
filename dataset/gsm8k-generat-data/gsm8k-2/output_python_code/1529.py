def solution():
    """Miles is going to spend 1/6 of a day reading. He will read comic books, graphic novels, and novels. He reads 21 pages an hour when he reads novels, 30 pages an hour when he reads graphic novels, and 45 pages an hour when he reads comic books. If he reads each for 1/3 of his time, how many pages does he read?"""
    total_reading_time = 1 / 6  # of a day
    novel_reading_time = total_reading_time / 3
    graphic_novel_reading_time = total_reading_time / 3
    comic_book_reading_time = total_reading_time / 3

    pages_read_from_novels = novel_reading_time * 21
    pages_read_from_graphic_novels = graphic_novel_reading_time * 30
    pages_read_from_comic_books = comic_book_reading_time * 45

    total_pages_read = pages_read_from_novels + pages_read_from_graphic_novels + pages_read_from_comic_books
    result = total_pages_read
    return result

print(solution())