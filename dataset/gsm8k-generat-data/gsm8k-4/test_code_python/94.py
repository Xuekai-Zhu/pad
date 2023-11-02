def solution():
    """John writes 20 pages a day. How long will it take him to write 3 books that are 400 pages each?"""
    # Define the number of pages John can write in a day
    pages_per_day = 20

    # Define the total number of pages John needs to write
    total_pages = 3 * 400

    # Calculate the number of days it will take John to write the books
    days_to_write = total_pages / pages_per_day

    # Return the result
    result = days_to_write
    return result

print(solution())