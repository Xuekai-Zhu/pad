def solution():
    """Tim buys a book of esoteric words. He learns 10 words from it a day. In 2 years the book has increased the number of words he knows by 50%. How many words did he know originally?"""
    words_learned_per_day = 10
    days_per_year = 365
    years = 2
    total_words_learned = words_learned_per_day * days_per_year * years
    percent_increase = 50
    original_words_known = total_words_learned / ((percent_increase / 100) + 1)
    result = original_words_known
    return result

print(solution())