def solution():
    """James writes from 1 PM to 4 PM every night.  He can write 5 pages per hour.  How many weeks will it take to finish his 735-page book?"""
    # Define James' writing speed in pages per hour
    WRITING_SPEED = 5

    # Calculate the total number of hours James will need to finish the book
    total_hours = 735 / (3 * WRITING_SPEED)

    # Calculate the number of weeks James will need to finish the book
    weeks = total_hours / 7

    # Display the number of weeks
    result = weeks
    return result

print(solution())