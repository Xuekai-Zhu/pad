def solution():
    """Sally reads 10 pages of a book on weekdays and 20 pages on weekends. If it takes 2 weeks for Sally to finish her book, how many pages that book has?"""
    weekdays = 5
    weekend_days = 2
    weekday_pages = 10
    weekend_pages = 20
    total_weekdays = weekdays * 2
    total_weekend_days = weekend_days * 2
    total_pages = (total_weekdays * weekday_pages) + (total_weekend_days * weekend_pages)
    result = total_pages
    return result

print(solution())