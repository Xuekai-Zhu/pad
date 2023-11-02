def solution():
    """Jenny wants to read 3 books in the next 10 days. She can read 100 words per hour. If the first book has 200 words, the second book has 400 words, and the third book has 300 words, how many minutes per day, on average, should she spend reading?"""
    # Define the total number of words to be read
    TOTAL_WORDS = 200 + 400 + 300

    # Calculate the total time needed to read all the books
    total_time = TOTAL_WORDS / 100

    # Calculate the average time per day needed to read all the books
    time_per_day = total_time / 10 * 60

    # Display the average time per day needed to read all the books
    result = time_per_day
    return result

print(solution())