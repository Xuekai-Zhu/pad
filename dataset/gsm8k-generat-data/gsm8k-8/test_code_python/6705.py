def solution():
    # Define Mark's original reading time and the increase
    original_reading_time = 2
    increase = 1.5

    # Calculate Mark's new reading time
    new_reading_time = original_reading_time + original_reading_time * increase

    # Define the number of pages Mark reads per day
    pages_per_day = 100

    # Calculate the number of pages Mark reads per week
    pages_per_week = new_reading_time * pages_per_day * 7
    result = pages_per_week
    return result

print(solution())