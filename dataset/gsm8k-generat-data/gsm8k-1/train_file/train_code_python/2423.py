def solution():
    """Bryan's score on a math exam is 20. Jen scored 10 more than Bryan while Sammy scored 2 fewer than Jen. If the math exam has 35 points in all, how many mistakes did Sammy make?"""
    bryan_score = 20
    jen_score = bryan_score + 10
    sammy_score = jen_score - 2
    total_score = 35
    total_mistakes = total_score - (bryan_score + jen_score + sammy_score)
    result = total_mistakes
    return result

print(solution())