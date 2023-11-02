def solution():
    # Define the total planned reading time in minutes
    planned_reading_time = 3 * 60

    # Calculate the actual reading time in minutes
    actual_reading_time = planned_reading_time * 0.75

    # Calculate the number of pages Rob read
    pages_read = actual_reading_time / 15

    result = pages_read
    return result

print(solution())