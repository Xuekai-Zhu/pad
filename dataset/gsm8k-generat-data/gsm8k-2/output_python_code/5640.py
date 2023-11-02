def solution():
    """Keenan needs to write an essay that is 1200 words. Her essay is due at midnight. She writes 400 words per hour for the first two hours. After that, she writes 200 words per hour. How many hours before the deadline does she need to start to finish on time?"""
    essay_words = 1200
    first_two_hours_speed = 400
    remaining_hours_speed = 200
    time_left = 0
    words_left = essay_words
    for i in range(1, 10):
        if i <= 2:
            time_left += 1
            words_left -= first_two_hours_speed
        else:
            time_left += 1
            words_left -= remaining_hours_speed
        if words_left <= 0:
            break
    result = 10 - time_left
    return result

print(solution())