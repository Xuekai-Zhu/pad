def solution():
    fraction_day_reading = 1/6
    hours_reading = fraction_day_reading * 24
    novel_hours = graphic_novel_hours = comic_hours = hours_reading / 3

    novel_pages_per_hour = 21
    graphic_novel_pages_per_hour = 30
    comic_pages_per_hour = 45

    # Calculate the total number of pages read for each type of book
    novel_pages = novel_hours * novel_pages_per_hour
    graphic_novel_pages = graphic_novel_hours * graphic_novel_pages_per_hour
    comic_pages = comic_hours * comic_pages_per_hour

    # Calculate the total number of pages read
    total_pages = novel_pages + graphic_novel_pages + comic_pages
    result = total_pages
    return result

print(solution())