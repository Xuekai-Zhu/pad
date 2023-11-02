def solution():
    words_per_minute = 5 * 25  # Rikki can write 25 words of poetry in 5 minutes
    words_per_hour = words_per_minute * 12  # There are 12 sets of 5 minutes in an hour
    total_words = words_per_hour * 2  # Rikki has 2 hours to write poetry

    # Calculate Rikki's potential earnings
    earnings = total_words * 0.01  # Rikki earns $.01 per word
    result = earnings
    return result

print(solution())