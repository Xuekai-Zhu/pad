def solution():
    """Sally reads 10 pages of a book on weekdays and 20 pages on weekends. If it takes 2 weeks for Sally to finish her book, how many pages that book has?"""
    weekdays_reading = 10 * 5 # 5 weekdays in a week
    weekend_reading = 20 * 2 # 2 weekends in a week
    total_reading = weekdays_reading + weekend_reading
    book_duration = 2 # 2 weeks
    total_pages = total_reading * book_duration
    result = total_pages
    return result

print(solution())