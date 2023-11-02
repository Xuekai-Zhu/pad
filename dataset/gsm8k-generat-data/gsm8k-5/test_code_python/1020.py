def solution():
    words_per_minute_right = 10  # Matt can write 10 words per minute with his right hand
    words_per_minute_left = 7  # Matt can write 7 words per minute with his left hand
    time = 5  # Matt writes for 5 minutes

    # Calculate the number of words Matt can write with his right hand in 5 minutes
    words_right = words_per_minute_right * time

    # Calculate the number of words Matt can write with his left hand in 5 minutes
    words_left = words_per_minute_left * time

    # Calculate the difference in the number of words written
    difference = words_right - words_left
    result = difference
    return result

print(solution())