def solution():
     word_limit = 1000
     words_written_sat = 450
     words_written_sun = 650
     total_words = words_written_sat + words_written_sun
     words_exceeded = total_words - word_limit
     result = words_exceeded
     return result

print(solution())