def solution():
    words_per_minute = 38  # Jaydee can type 38 words in a minute
    total_words = 4560  # The research paper has 4560 words

    # Calculate the time it will take Jaydee to finish typing the paper in minutes
    time_in_minutes = total_words / words_per_minute

    # Convert the time to hours
    time_in_hours = time_in_minutes / 60
    result = time_in_hours
    return result

print(solution())