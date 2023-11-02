def solution():
    """Abigail has a report due tomorrow which needs to be 1000 words in length. Abigail can type 300 words in half an hour. If she has already written 200 words, how many more minutes will it take her to finish the report?"""
    report_length = 1000
    typing_speed = 300 / 30  # convert to words per minute
    words_written = 200
    remaining_words = report_length - words_written
    time_to_finish = remaining_words / typing_speed
    result = time_to_finish
    return result

print(solution())