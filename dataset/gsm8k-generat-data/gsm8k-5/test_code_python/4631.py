def solution():
    words_per_article = 600  # Reporter writes 600 words per article
    cost_per_word = 0.1  # Reporter earns 10 cents per word
    cost_per_article = 60  # Reporter earns $60 per article

    articles_to_write = 3  # Reporter has to finish 3 articles
    total_words = articles_to_write * words_per_article  # Total words to write
    total_time = 4  # Reporter has 4 hours to write
    total_minutes = total_time * 60  # Total minutes to write
    words_per_minute = 10  # Reporter writes 10 words per minute

    # Calculate the total earnings
    earnings_per_article = words_per_article * cost_per_word + cost_per_article
    total_earnings = earnings_per_article * articles_to_write

    # Calculate expected earnings per hour
    expected_earnings_per_hour = total_earnings / total_time
    result = expected_earnings_per_hour
    return result

print(solution())