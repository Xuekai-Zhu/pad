def solution():
    total_hours = 8
    movie1_hours = 3.5
    movie2_hours = 1.5

    # Calculate the remaining time for reading
    reading_hours = total_hours - movie1_hours - movie2_hours

    # Calculate the total time in minutes for reading
    reading_minutes = reading_hours * 60

    # Calculate the total number of words that Henri can read in the remaining time
    num_words = reading_minutes * 10
    result = num_words
    return result

print(solution())