def solution():
    """James writes from 1 PM to 4 PM every night. He can write 5 pages per hour. How many weeks will it take to finish his 735-page book?"""
    # Define the number of hours James writes each night
    hours_per_night = 3

    # Define the number of pages James can write per hour
    pages_per_hour = 5

    # Define the total number of pages in the book
    total_pages = 735

    # Calculate the total number of hours it will take to finish the book
    total_hours = total_pages / (hours_per_night * pages_per_hour)

    # Calculate the total number of weeks it will take to finish the book
    total_weeks = total_hours / 7

    # Round up to the nearest week
    total_weeks = math.ceil(total_weeks)

    result = total_weeks
    return result

print(solution())