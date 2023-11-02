def solution():
    start_time = 1  # 1 PM
    end_time = 4  # 4 PM
    num_hours_per_night = end_time - start_time
    pages_per_hour = 5

    total_pages = 735

    # Calculate the total number of hours needed to finish the book
    total_hours = total_pages / pages_per_hour

    # Calculate the total number of weeks needed to finish the book
    total_weeks = total_hours / (num_hours_per_night * 7)
    result = total_weeks
    return result

print(solution())