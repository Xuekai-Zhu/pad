def solution():
    
    words_per_minute = 5
    words_per_sprint = 25
    total_sprints = (2 * 60) / 5
    total_words = total_sprints * words_per_sprint
    earnings_per_word = 0.01
    total_earnings = total_words * earnings_per_word
    result = total_earnings
    return result

print(solution())