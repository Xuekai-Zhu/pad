def solution():
    
    hours_reading = 1/6 * 24
    novel_hours = graphic_novel_hours = comic_hours = hours_reading / 3
    novel_pages = 21 * novel_hours
    graphic_novel_pages = 30 * graphic_novel_hours
    comic_pages = 45 * comic_hours
    total_pages = novel_pages + graphic_novel_pages + comic_pages
    result = total_pages
    return result

print(solution())