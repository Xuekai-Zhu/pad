def solution():
    """Rikki is writing and selling poetry. He sells his poems for $.01 a word. He can write 25 words of poetry in 5 minutes. If he has 2 hours to write poetry, how much can he expect to earn?"""
    words_per_minute = 5
    words_per_5_min = 25
    words_per_hour = words_per_5_min * 12
    total_words = words_per_hour * 2
    price_per_word = 0.01
    total_earnings = total_words * price_per_word
    result = total_earnings
    return result

print(solution())