def solution():
    
    words_per_minute = 5
    words_per_5_min = 25
    words_per_hour = words_per_5_min * 12
    total_words = words_per_hour * 2
    price_per_word = 0.01
    total_earnings = total_words * price_per_word
    result = total_earnings
    return result

print(solution())