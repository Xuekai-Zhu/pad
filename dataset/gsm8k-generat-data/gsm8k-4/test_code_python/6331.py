def solution():
    """Anna can read 1 page in 1 minute. Carole can read as fast as Anna but at half the speed of Brianna. How long does it take Brianna to read a 100-page book?"""
    # Define the reading speeds of Anna and Brianna
    anna_speed = 1  # page per minute
    brianna_speed = 2 * anna_speed  # pages per minute
    
    # Calculate the time it takes Brianna to read a 100-page book
    book_pages = 100
    brianna_time = book_pages / brianna_speed  # minutes
    
    # return the result
    result = brianna_time
    return result

print(solution())