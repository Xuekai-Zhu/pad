def solution():
    
    total_time = 8
    movie1_time = 3.5
    movie2_time = 1.5
    reading_time = total_time - (movie1_time + movie2_time)
    words_per_minute = 10
    total_words_read = reading_time * 60 * words_per_minute
    result = total_words_read
    return result

print(solution())