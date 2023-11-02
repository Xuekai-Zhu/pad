def solution():
    """Keenan needs to write an essay that is 1200 words. Her essay is due at midnight. She writes 400 words per hour for the first two hours. After that, she writes 200 words per hour. How many hours before the deadline does she need to start to finish on time?"""
    # Define the total number of words Keenan needs to write
    total_words = 1200

    # Define Keenan's initial writing speed
    initial_speed = 400  # in words per hour

    # Define the time Keenan spent writing at her initial speed
    initial_time = 2  # in hours

    # Define Keenan's reduced writing speed
    reduced_speed = 200  # in words per hour

    # Calculate the number of words Keenan has already written
    initial_words = initial_speed * initial_time

    # Calculate the number of remaining words
    remaining_words = total_words - initial_words

    # Calculate the time it will take to write the remaining words
    reduced_time = remaining_words / reduced_speed

    # Calculate the total time needed to finish the essay
    total_time = initial_time + reduced_time

    # Display the hours before the deadline Keenan needs to start
    result = 12 - total_time  # assuming the deadline is at midnight
    return result

print(solution())