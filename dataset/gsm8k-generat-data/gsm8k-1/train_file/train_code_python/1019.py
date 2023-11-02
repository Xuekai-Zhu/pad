def solution():
    """Matt can write 10 words a minute with his right hand and 7 words a minute with his left hand. How many words would Matt write in 5 minutes with his right hand than with his left?"""
    words_per_minute_right = 10
    words_per_minute_left = 7
    time_in_minutes = 5
    words_written_right = words_per_minute_right * time_in_minutes
    words_written_left = words_per_minute_left * time_in_minutes
    difference = words_written_right - words_written_left
    result = difference
    return result

print(solution())