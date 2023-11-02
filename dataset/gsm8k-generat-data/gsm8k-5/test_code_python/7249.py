def solution():
    words_on_saturday = 450  # Vinnie wrote 450 words on Saturday
    words_on_sunday = 650  # Vinnie wrote 650 words on Sunday
    total_words = words_on_saturday + words_on_sunday  # Total number of words Vinnie wrote
    limit = 1000  # Word limit for the essay

    # Calculate the number of words Vinnie has exceeded the limit by
    exceeded_words = total_words - limit
    result = exceeded_words
    return result

print(solution())