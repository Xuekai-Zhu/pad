def solution():
    # Calculate the total number of words in all three books
    total_words = 200 + 400 + 300

    # Calculate the total time needed to read all three books in hours
    total_time_hours = total_words / 100

    # Calculate the average daily reading time in minutes
    avg_reading_time_minutes = (total_time_hours / 10) * 60

    result = avg_reading_time_minutes
    return result

print(solution())