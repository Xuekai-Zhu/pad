def solution():
    """Carolyn is planning out her final essay. The introduction will be 450 words, the conclusion will be triple the length of the introduction, and each of the four body sections will be the same length. If her essay has to be 5000 words total, how long is each section?"""
    intro_length = 450
    conclusion_length = intro_length * 3
    body_length = (5000 - intro_length - conclusion_length) / 4
    result = body_length
    return result

print(solution())