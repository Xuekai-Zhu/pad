def solution():
    """Rikki is writing and selling poetry. He sells his poems for $.01 a word. He can write 25 words of poetry in 5 minutes. If he has 2 hours to write poetry, how much can he expect to earn?"""
    # Convert 2 hours to minutes
    total_time = 2 * 60

    # Calculate the number of words Rikki can write in the given time
    words_written = (total_time / 5) * 25

    # Calculate the earnings from selling the written words
    earnings = words_written * 0.01

    # Round the earnings to 2 decimal places
    rounded_earnings = round(earnings, 2)

    # return the result
    result = rounded_earnings
    return result

print(solution())