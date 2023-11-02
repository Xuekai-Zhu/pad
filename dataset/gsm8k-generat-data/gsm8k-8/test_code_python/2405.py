def solution():
    # Calculate the time it takes for Lily to type 1 word
    time_per_word = 1 / 15

    # Calculate the time it takes for Lily to type 10 words (without breaks)
    time_per_10_words = time_per_word * 10

    # Calculate the total time it takes for Lily to type 255 words
    num_10_word_groups = 255 // 10
    total_time = (num_10_word_groups * time_per_10_words) + ((num_10_word_groups - 1) * 2)

    # Add on the remaining words (if any)
    remaining_words = 255 % 10
    total_time += remaining_words * time_per_word

    result = total_time
    return result

print(solution())