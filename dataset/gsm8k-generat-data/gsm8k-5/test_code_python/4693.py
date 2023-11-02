def solution():
    original_speed = 212  # Barbara's original typing speed
    reduced_speed = original_speed - 40  # Barbara's reduced typing speed
    total_words = 3440  # The total number of words Barbara needs to type

    # Calculate the time it would take Barbara to type the document at her original speed
    time_original = total_words / original_speed

    # Calculate the time it would take Barbara to type the document at her reduced speed
    time_reduced = total_words / reduced_speed

    # The time it would take Barbara is the maximum of the two times calculated above
    time = max(time_original, time_reduced)
    result = time
    return result

print(solution())