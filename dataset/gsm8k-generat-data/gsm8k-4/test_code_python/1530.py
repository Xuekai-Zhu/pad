def solution():
    """Miles is going to spend 1/6 of a day reading. He will read comic books, graphic novels, and novels. He reads 21 pages an hour when he reads novels, 30 pages an hour when he reads graphic novels, and 45 pages an hour when he reads comic books. If he reads each for 1/3 of his time, how many pages does he read?"""
    # Define the time Miles will spend reading and the number of pages he reads per hour for each type of book
    reading_time = 1 / 6
    novel_pages_per_hour = 21
    graphic_novel_pages_per_hour = 30
    comic_pages_per_hour = 45

    # Calculate the total number of pages read for each type of book
    novel_pages = novel_pages_per_hour * reading_time * (1 / 3)
    graphic_novel_pages = graphic_novel_pages_per_hour * reading_time * (1 / 3)
    comic_pages = comic_pages_per_hour * reading_time * (1 / 3)

    # Calculate the total number of pages read
    total_pages = novel_pages + graphic_novel_pages + comic_pages

    # Round the result to the nearest integer
    result = round(total_pages)
    return result

print(solution())