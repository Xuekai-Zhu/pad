def solution():
    words_per_minute = 60
    total_words = 10800

    # Calculate the total time in minutes it takes to type all the words
    total_time_in_minutes = total_words / words_per_minute

    # Convert the total time in minutes to hours
    total_time_in_hours = total_time_in_minutes / 60

    result = total_time_in_hours
    return result

print(solution())