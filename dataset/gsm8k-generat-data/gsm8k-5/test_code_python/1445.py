def solution():
    total_books = 3  # Jenny wants to read 3 books
    total_days = 10  # Jenny has 10 days to read the books
    total_words = 200 + 400 + 300  # Total number of words in all the books combined
    words_per_hour = 100  # Jenny can read 100 words per hour

    # Calculate the total time required to read all the books
    total_time_hours = total_words / words_per_hour
    total_time_minutes = total_time_hours * 60

    # Calculate the average time required per day to read the books
    average_time_minutes = total_time_minutes / total_days
    result = average_time_minutes
    return result

print(solution())