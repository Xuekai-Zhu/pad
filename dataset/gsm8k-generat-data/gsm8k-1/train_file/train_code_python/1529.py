def solution():
    """Miles is going to spend 1/6 of a day reading. He will read comic books, graphic novels, and novels. He reads 21 pages an hour when he reads novels, 30 pages an hour when he reads graphic novels, and 45 pages an hour when he reads comic books. If he reads each for 1/3 of his time, how many pages does he read?"""
    hours_reading = 1/6 * 24
    novel_hours = graphic_novel_hours = comic_hours = hours_reading / 3
    novel_pages = 21 * novel_hours
    graphic_novel_pages = 30 * graphic_novel_hours
    comic_pages = 45 * comic_hours
    total_pages = novel_pages + graphic_novel_pages + comic_pages
    result = total_pages
    return result

print(solution())