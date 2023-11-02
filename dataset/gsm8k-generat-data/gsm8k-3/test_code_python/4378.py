def solution():
    """Rikki is writing and selling poetry. He sells his poems for $.01 a word. He can write 25 words of poetry in 5 minutes. If he has 2 hours to write poetry, how much can he expect to earn?"""
    # Define Rikki's writing rate in words per minute
    RATE = 5  # 25 words in 5 minutes

    # Calculate the total number of words Rikki can write in 2 hours
    total_words = RATE * 24 * 2  # 24 5-minute increments in 2 hours

    # Calculate Rikki's expected earnings
    earnings = total_words * 0.01

    # Display Rikki's expected earnings
    result = earnings
    return result

print(solution())