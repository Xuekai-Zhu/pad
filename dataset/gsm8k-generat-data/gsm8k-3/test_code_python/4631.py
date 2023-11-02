def solution():
    """A reporter is paid by the word and per article. She earns $.1 per word. She earns $60 per article. She has to finish three stories in the next 4 hours. She averages 10 words a minute. How much can she expect to earn per hour if she writes the entire time?"""
    # Define the pay rate per word and per article
    WORD_RATE = 0.1
    ARTICLE_RATE = 60

    # Define the number of articles to write
    articles_to_write = 3

    # Define the time available to write
    time_available = 4 * 60 # convert hours to minutes

    # Define the average words written per minute
    words_per_minute = 10

    # Calculate the total time needed to write all the articles
    time_needed = articles_to_write * ARTICLE_RATE / (WORDS_PER_MINUTE * WORD_RATE)

    # If the time needed is greater than the time available, adjust the number of articles to write
    if time_needed > time_available:
        articles_to_write = time_available * (WORDS_PER_MINUTE * WORD_RATE) / ARTICLE_RATE
        time_needed = time_available

    # Calculate the total earnings
    earnings = articles_to_write * ARTICLE_RATE + (WORDS_PER_MINUTE * WORD_RATE) * time_needed

    # Calculate the earnings per hour
    earnings_per_hour = earnings / (time_available / 60)

    # Return the earnings per hour
    result = earnings_per_hour
    return result

print(solution())