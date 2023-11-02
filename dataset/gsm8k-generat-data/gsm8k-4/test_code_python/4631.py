def solution():
    """A reporter is paid by the word and per article. She earns $.1 per word. She earns $60 per article. She has to finish three stories in the next 4 hours. She averages 10 words a minute. How much can she expect to earn per hour if she writes the entire time?"""
    # Define the pay rate per word and per article
    WORD_RATE = 0.1
    ARTICLE_RATE = 60

    # Define the time available to write
    TIME_AVAILABLE = 4 * 60 # 4 hours in minutes

    # Define the number of stories to write
    num_stories = 3

    # Define the average words written per minute
    words_per_minute = 10

    # Calculate the total words that need to be written
    total_words = num_stories * 1000

    # Calculate the total pay for writing the articles
    total_pay = (total_words * WORD_RATE) + (num_stories * ARTICLE_RATE)

    # Calculate the time needed to write all the articles
    time_needed = total_words / words_per_minute

    # Calculate the pay per hour when writing the entire time
    pay_per_hour = (total_pay / (TIME_AVAILABLE - time_needed)) * 60

    result = pay_per_hour
    return result

print(solution())