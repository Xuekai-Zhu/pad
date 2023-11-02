def solution():
    # Calculate the number of pages Jo read in the past hour
    pages_read_in_past_hour = 90 - 60

    # Calculate the total number of pages Jo still needs to read
    pages_left_to_read = 210 - 90

    # Calculate the total number of hours Jo will be reading the book
    total_hours = pages_left_to_read / pages_read_in_past_hour
    result = total_hours
    return result

print(solution())