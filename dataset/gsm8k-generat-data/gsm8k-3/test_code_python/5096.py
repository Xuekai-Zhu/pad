def solution():
    """Sally reads 10 pages of a book on weekdays and 20 pages on weekends. If it takes 2 weeks for Sally to finish her book, how many pages that book has?"""
    # Define the number of pages Sally reads on weekdays and weekends
    WEEKDAY_PAGES = 10
    WEEKEND_PAGES = 20

    # Define the number of weekdays and weekends in a week
    WEEKDAYS = 5
    WEEKENDS = 2

    # Define the number of weeks it takes Sally to finish the book
    weeks = 2

    # Calculate the total number of pages in the book
    total_pages = weeks * (WEEKDAYS * WEEKDAY_PAGES + WEEKENDS * WEEKEND_PAGES)

    # Display the total number of pages in the book
    result = total_pages
    return result

print(solution())