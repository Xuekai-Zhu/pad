def solution():
    """Tim buys a book of esoteric words. He learns 10 words from it a day. In 2 years the book has increased the number of words he knows by 50%. How many words did he know originally?"""
    words_per_day = 10
    days_in_2_years = 730
    total_words_learned = days_in_2_years * words_per_day
    original_words_known = total_words_learned / 1.5 - total_words_learned
    result = original_words_known
    return result

print(solution())