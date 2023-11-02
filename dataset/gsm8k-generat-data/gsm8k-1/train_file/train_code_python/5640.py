def solution():
    """Keenan needs to write an essay that is 1200 words. Her essay is due at midnight. She writes 400 words per hour for the first two hours. After that, she writes 200 words per hour. How many hours before the deadline does she need to start to finish on time?"""
    total_words = 1200
    words_per_hour_1 = 400
    hours_1 = 2
    words_per_hour_2 = 200
    words_written = (words_per_hour_1 * hours_1) + (words_per_hour_2 * (total_words - (words_per_hour_1 * hours_1)))
    time_needed = ((total_words - words_written) / words_per_hour_2)
    result = time_needed
    return result

print(solution())