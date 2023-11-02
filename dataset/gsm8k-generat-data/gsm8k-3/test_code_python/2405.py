def solution():
    """Lily types 15 words a minute and takes a 2-minute break every 10 minutes. How long does it take for Lily to type 255 words?"""
    # Calculate the number of minutes it takes Lily to type the first 10 minutes worth of words
    first_10_min_words = 10 * 15
    first_10_min_time = 10 + 2 # 10 minutes of typing and 2 minutes of break time
    remaining_words = 255 - first_10_min_words

    # Calculate the number of full 10-minute typing periods required to finish the remaining words
    full_periods = remaining_words // (10 * 15)
    full_time = full_periods * (10 + 2)

    # Calculate the time required to type the remaining words
    remaining_time = (remaining_words % (10 * 15)) / 15

    # Calculate the total time required
    total_time = first_10_min_time + full_time + remaining_time

    # Display the total time required
    result = total_time
    return result

print(solution())