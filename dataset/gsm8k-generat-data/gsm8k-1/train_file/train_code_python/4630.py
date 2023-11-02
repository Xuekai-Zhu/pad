def solution():
    """A reporter is paid by the word and per article. She earns $.1 per word. She earns $60 per article. She has to finish three stories in the next 4 hours. She averages 10 words a minute. How much can she expect to earn per hour if she writes the entire time?"""
    pay_per_word = 0.1
    pay_per_article = 60
    num_articles = 3
    num_hours = 4
    num_words = num_articles * 1000 #assuming an average article is 1000 words
    time_written = num_words / 10 #assuming 10 words per minute
    time_left = num_hours * 60 - time_written
    earnings = num_words * pay_per_word + num_articles * pay_per_article
    earnings_per_hour = earnings / (num_hours + time_left / 60)
    
    result = earnings_per_hour
    return result

print(solution())