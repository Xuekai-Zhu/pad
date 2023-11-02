def solution():
    """Rikki is writing and selling poetry. He sells his poems for $.01 a word. He can write 25 words of poetry in 5 minutes. If he has 2 hours to write poetry, how much can he expect to earn?"""
    words_per_minute = 5
    words_per_sprint = 25
    total_sprints = (2 * 60) / 5
    total_words = total_sprints * words_per_sprint
    earnings_per_word = 0.01
    total_earnings = total_words * earnings_per_word
    result = total_earnings
    return result

print(solution())