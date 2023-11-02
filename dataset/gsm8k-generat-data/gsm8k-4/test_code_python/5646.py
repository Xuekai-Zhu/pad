def solution():
    """Steve decides to read a new book. He reads 100 pages Monday, Wed, and Friday. The book is 2100 pages long. How many weeks does it take to read them all?"""
    # Define the number of pages read per week
    weekly_pages = 300

    # Define the total number of pages in the book
    total_pages = 2100

    # Calculate the number of weeks it will take to read the book
    weeks_to_read = total_pages / weekly_pages

    # return the result
    result = weeks_to_read
    return result

print(solution())