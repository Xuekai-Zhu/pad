def solution():
    # Calculate the remaining words that Abigail needs to type
    remaining_words = 1000 - 200  # she has already written 200 words

    # Calculate how many half-hours Abigail needs to type for
    half_hours_needed = remaining_words/300

    # Convert the half-hours to minutes
    minutes_needed = half_hours_needed * 30

    result = minutes_needed
    return result

print(solution())