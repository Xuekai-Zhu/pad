def solution():
    """Keenan needs to write an essay that is 1200 words. Her essay is due at midnight. She writes 400 words per hour for the first two hours. After that, she writes 200 words per hour. How many hours before the deadline does she need to start to finish on time?"""
    # Define the target word count and the writing speed
    TARGET_WORD_COUNT = 1200
    INITIAL_WRITING_SPEED = 400
    LATER_WRITING_SPEED = 200

    # Define the time Keenan has before the deadline
    TIME_BEFORE_DEADLINE = 0

    # Calculate the number of words written in the first two hours
    first_two_hours_word_count = INITIAL_WRITING_SPEED * 2

    # Calculate the remaining number of words to write
    remaining_word_count = TARGET_WORD_COUNT - first_two_hours_word_count

    # Calculate the time Keenan needs to write the remaining words
    if remaining_word_count <= 0:
        time_to_write_remaining_words = 0
    else:
        time_to_write_remaining_words = remaining_word_count / LATER_WRITING_SPEED

    # Calculate the total time Keenan needs to finish the essay
    total_time = 2 + time_to_write_remaining_words

    # Calculate the time Keenan needs to start writing
    TIME_BEFORE_DEADLINE = total_time
    result = TIME_BEFORE_DEADLINE
    return result

print(solution())