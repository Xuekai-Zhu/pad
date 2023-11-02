def solution():
    """Bryan's score on a math exam is 20. Jen scored 10 more than Bryan while Sammy scored 2 fewer than Jen. If the math exam has 35 points in all, how many mistakes did Sammy make?"""
    bryans_score = 20
    jens_score = bryans_score + 10
    sammies_score = jens_score - 2
    total_points = 35
    mistakes = total_points - (bryans_score + jens_score + sammies_score)
    result = mistakes
    return result

print(solution())