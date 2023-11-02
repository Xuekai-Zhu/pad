def solution():
    
    word_limit = 1000
    saturday_words = 450
    sunday_words = 650
    total_words = saturday_words + sunday_words
    exceeded_words = max(total_words - word_limit, 0)
    result = exceeded_words
    return result

print(solution())