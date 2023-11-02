def solution():
    """Steve decides to read a new book.  He reads 100 pages Monday, Wed, and Friday.  The book is 2100 pages long.  How many weeks does it take to read them all?"""
    # Define the number of pages read each week
    pages_per_week = 300 # 100 pages on Mon, Wed, and Fri

    # Define the total number of pages in the book
    total_pages = 2100

    # Calculate the number of weeks it takes to read the entire book
    weeks_to_read = total_pages // pages_per_week

    # Display the number of weeks it takes to read the entire book
    result = weeks_to_read
    return result

print(solution())