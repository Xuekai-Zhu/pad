def solution():
    """Jenny wants to read 3 books in the next 10 days. She can read 100 words per hour.
    If the first book has 200 words, the second book has 400 words, and the third book has 300 words,
    how many minutes per day, on average, should she spend reading?"""
    # Define the total number of words to be read.
    total_words = 200 + 400 + 300

    # Calculate the time needed to read all the books in hours.
    total_time_hours = total_words / 100

    # Calculate the time needed to read all the books in minutes.
    total_time_minutes = total_time_hours * 60

    # Calculate the average time needed to read per day in minutes.
    average_time_per_day = total_time_minutes / 10

    # Return the result
    result = average_time_per_day
    return result

print(solution())