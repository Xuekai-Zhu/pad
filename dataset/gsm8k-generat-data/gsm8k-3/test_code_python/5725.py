def solution():
    """Tim buys a book of esoteric words.  He learns 10 words from it a day.  In 2 years the book has increased the number of words he knows by 50%.  How many words did he know originally?"""
    # Calculate the number of days in 2 years
    days = 2 * 365

    # Calculate the number of words Tim learns in 2 years
    words_learned = 10 * days

    # Calculate the percentage increase in Tim's knowledge of words
    increase_percent = 50

    # Calculate the original number of words Tim knew
    original_words = words_learned / (1 + increase_percent/100)

    # Display the original number of words Tim knew
    result = original_words
    return result

print(solution())