def solution():
    """Sally reads 10 pages of a book on weekdays and 20 pages on weekends. If it takes 2 weeks for Sally to finish her book, how many pages that book has?"""
    # Define the number of weekdays and weekends in a week
    WEEKDAYS = 5
    WEEKENDS = 2

    # Calculate the total number of pages read in a week
    pages_per_week = (10 * WEEKDAYS) + (20 * WEEKENDS)

    # Calculate the total number of pages in the book
    total_pages = pages_per_week * 2

    result = total_pages
    return result

print(solution())