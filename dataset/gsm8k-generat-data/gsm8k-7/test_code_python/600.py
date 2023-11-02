def solution():
    original_speed = 65
    reduced_speed = 45
    total_words = 810

    # Calculate the number of words that Mike can type per minute with his reduced speed
    words_per_minute = reduced_speed

    # Calculate the total time in minutes that it will take Mike to finish typing the document
    total_time = total_words / words_per_minute
    result = total_time
    return result

print(solution())