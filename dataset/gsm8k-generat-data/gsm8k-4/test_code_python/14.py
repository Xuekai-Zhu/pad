def solution():
    """Joy can read 8 pages of a book in 20 minutes. How many hours will it take her to read 120 pages?"""
    # Calculate Joy's reading rate per page
    pages_per_minute = 8 / 20

    # Calculate the total number of minutes it will take Joy to read 120 pages
    total_minutes = 120 / pages_per_minute

    # Calculate the total number of hours it will take Joy to read 120 pages
    total_hours = total_minutes / 60

    # Round the result to 2 decimal places
    result = round(total_hours, 2)
    return result

print(solution())