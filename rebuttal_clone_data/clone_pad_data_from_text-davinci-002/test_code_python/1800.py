def solution():
    leo_mistakes = 2
    madeline_mistakes = leo_mistakes / 2
    brent_mistakes = leo_mistakes + 1
    brent_score = 25
    difference = brent_score - brent_mistakes
    madeline_score = difference - madeline_mistakes
    result = madeline_score
    return result

print(solution())