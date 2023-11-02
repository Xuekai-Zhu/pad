def solution():
    """Abigail has a report due tomorrow which needs to be 1000 words in length. Abigail can type 300 words in half an hour. If she has already written 200 words, how many more minutes will it take her to finish the report?"""
    words_needed = 1000
    words_per_minute = 10
    time_taken = ((words_needed - 200) / words_per_minute) * 30
    result = time_taken
    return result

print(solution())