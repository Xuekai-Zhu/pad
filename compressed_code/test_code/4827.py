def solution():
    
    report_length = 1000
    typing_speed = 300 / 30  
    words_written = 200
    remaining_words = report_length - words_written
    time_to_finish = remaining_words / typing_speed
    result = time_to_finish
    return result

print(solution())