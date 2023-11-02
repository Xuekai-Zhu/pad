def solution():
    # Calculate the total time Rikki has to write poetry
    total_time = 2 * 60  # 2 hours converted to minutes

    # Calculate the number of words Rikki can write in the given time
    words_written = (total_time / 5) * 25  # Rikki can write 25 words of poetry in 5 minutes

    # Calculate the expected earnings
    expected_earnings = words_written * 0.01

    result = expected_earnings
    return result

print(solution())