def solution():
    """In a Geometry exam, Madeline got 2 mistakes which are half as many mistakes as Leo. Brent scored 25 and has 1 more mistake than Leo. What is Madeline's score?"""
    leo_mistakes = (25 - 1) / 2
    madeline_mistakes = 2
    total_mistakes = leo_mistakes + madeline_mistakes
    madeline_score = 100 - (total_mistakes * 5)
    result = madeline_score
    return result

print(solution())