def solution():
    books_to_read = 3
    days_to_read = 10
    words_per_hour = 100
    book1_word_count = 200
    book2_word_count = 400
    book3_word_count = 300
    total_words = book1_word_count + book2_word_count + book3_word_count
    hours_needed = total_words / words_per_hour
    minutes_needed_per_day = (hours_needed / days_to_read) * 60
    result = minutes_needed_per_day
    return result

print(solution())