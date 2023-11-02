def solution():
    """Carolyn is planning out her final essay. The introduction will be 450 words, the conclusion will be triple the length of the introduction, and each of the four body sections will be the same length. If her essay has to be 5000 words total, how long is each section?"""
    total_words = 5000
    intro_words = 450
    conclusion_words = 3 * intro_words
    body_words = (total_words - intro_words - conclusion_words) / 4
    result = body_words
    return result

print(solution())