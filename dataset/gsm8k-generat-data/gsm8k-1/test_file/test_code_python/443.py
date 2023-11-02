def solution():
    """Joey has 214 points before his turn in Scrabble. He scores 26 points. Then Marcy, who has 225 points, scores 10 points. By how many points is Joey now winning?"""
    joey_points = 214 + 26
    marcy_points = 225 + 10
    diff = joey_points - marcy_points
    result = diff
    return result

print(solution())