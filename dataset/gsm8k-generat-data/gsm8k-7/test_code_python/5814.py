def solution():
    total_reading_time = 60  # 1 hour of reading
    friday_reading_time = 16
    saturday_reading_time = 28

    # Calculate the reading time left for Sunday
    sunday_reading_time = total_reading_time - friday_reading_time - saturday_reading_time
    result = sunday_reading_time
    return result

print(solution())