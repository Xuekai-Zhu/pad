def solution():
    
    days = 730
    words_learned_per_day = 10
    total_words_learned = days * words_learned_per_day
    percent_increase = 50
    increase_amount = total_words_learned * (percent_increase / 100)
    final_word_total = total_words_learned + increase_amount
    original_words = final_word_total / 2
    result = original_words
    
    return result

print(solution())