def solution():
    # Calculate the number of minutes Rikki has to write poetry
    total_minutes = 2 * 60

    # Calculate the number of 5-minute intervals Rikki has to write poetry
    num_intervals = total_minutes // 5

    # Calculate the number of words Rikki can write in 2 hours
    total_words = num_intervals * 25

    # Calculate Rikki's expected earnings
    expected_earnings = total_words * 0.01
    result = expected_earnings
    return result

print(solution())