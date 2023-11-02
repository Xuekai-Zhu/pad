def solution():
    """Joy can read 8 pages of a book in 20 minutes. How many hours will it take her to read 120 pages?"""
    # Define the reading speed in pages per minute
    speed = 8 / 20  # pages per minute

    # Calculate the total reading time in minutes
    total_reading_time = 120 / speed

    # Convert the reading time to hours
    hours = total_reading_time / 60

    # Return the result
    result = hours
    return result

print(solution())