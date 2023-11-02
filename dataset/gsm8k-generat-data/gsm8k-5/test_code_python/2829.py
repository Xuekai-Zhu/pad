def solution():
    total_reading_time = 3  # Rob planned on spending 3 hours reading
    actual_reading_time = total_reading_time * 0.75  # Rob only spends 75% of the planned reading time

    # Calculate the total number of pages Rob read
    pages_per_minute = 4  # Rob reads 1 page every 15 minutes
    total_reading_pages = pages_per_minute * 60 * actual_reading_time

    result = total_reading_pages
    return result

print(solution())