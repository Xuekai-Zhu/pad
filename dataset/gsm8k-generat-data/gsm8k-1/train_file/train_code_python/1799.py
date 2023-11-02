def solution():
    """In a Geometry exam, Madeline got 2 mistakes which are half as many mistakes as Leo. Brent scored 25 and has 1 more mistake than Leo. What is Madeline's score?"""
    brent_score = 25
    leo_mistakes = brent_score - 1
    madeline_mistakes = leo_mistakes / 2
    madeline_score = brent_score - madeline_mistakes
    result = madeline_score
    return result

print(solution())