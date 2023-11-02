def solution():
    report_length = 1000  # Abigail's report needs to be 1000 words
    typing_speed = 600  # Abigail's typing speed is 300 words per 30 minutes
    words_written = 200  # Abigail has already written 200 words

    # Calculate how many words she still needs to write
    words_left = report_length - words_written

    # Calculate how long it will take Abigail to finish typing the remaining words
    time_left = (words_left / typing_speed) * 60

    result = time_left
    return result

print(solution())