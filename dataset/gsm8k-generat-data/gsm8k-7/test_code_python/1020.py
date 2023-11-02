def solution():
    words_per_minute_right = 10
    words_per_minute_left = 7
    time_in_minutes = 5

    # Calculate the total number of words that Matt can write with his right hand in 5 minutes
    words_with_right_hand = words_per_minute_right * time_in_minutes

    # Calculate the total number of words that Matt can write with his left hand in 5 minutes
    words_with_left_hand = words_per_minute_left * time_in_minutes

    # Calculate the difference in words between Matt's right and left hand in 5 minutes
    difference = words_with_right_hand - words_with_left_hand
    result = difference
    return result

print(solution())