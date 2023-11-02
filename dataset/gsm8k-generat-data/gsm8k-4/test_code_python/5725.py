def solution():
    """Tim buys a book of esoteric words. He learns 10 words from it a day. In 2 years the book has increased the number of words he knows by 50%. How many words did he know originally?"""
    # Define the daily number of words Tim learns
    daily_words = 10

    # Calculate the total number of words Tim learns in 2 years
    words_in_2_years = daily_words * 365 * 2

    # Calculate the percentage increase in Tim's vocabulary
    increase_percentage = 50

    # Calculate the total number of words Tim knew originally
    original_words = words_in_2_years / (1 + (increase_percentage / 100))

    result = original_words
    return result

print(solution())