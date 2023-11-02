def solution():
    
    total_words = 5000
    intro_words = 450
    conclusion_words = 3 * intro_words
    body_words = (total_words - intro_words - conclusion_words) / 4
    result = body_words
    return result

print(solution())