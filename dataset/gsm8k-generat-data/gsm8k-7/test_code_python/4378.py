def solution():
    words_per_minute = 5*25
    words_per_hour = words_per_minute * 12
    total_words = words_per_hour * 2
    earnings_per_word = 0.01
    total_earnings = earnings_per_word * total_words
    result = total_earnings
    return result

print(solution())