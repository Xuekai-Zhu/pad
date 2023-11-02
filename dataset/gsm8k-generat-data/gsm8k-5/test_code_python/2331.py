def solution():
    total_time = 8  # Henri has 8 hours
    movie1_time = 3.5  # Henri watches a movie that is 3.5 hours
    movie2_time = 1.5  # Henri watches another movie that is 1.5 hours
    reading_time = total_time - movie1_time - movie2_time  # Henri has the remaining time to read

    # Calculate the total time Henri spends reading in minutes
    total_reading_time = reading_time * 60
    # Calculate the total number of words Henri can read
    total_words_read = total_reading_time * 10
    result = total_words_read
    return result

print(solution())