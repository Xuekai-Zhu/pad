def solution():
    """Clyde's four children wanted to go see their favorite band perform. The tickets were expensive so Clyde made a deal with his kids. If the average of their scores on their next math test was higher than 89, then he would buy them tickets to the concert. June earned a 97 on her math test, Patty earned an 85, Josh earned a 100 on his test and Henry earned a 94. What was their average math test score?"""
    test_scores = [97, 85, 100, 94]
    average_score = sum(test_scores) / len(test_scores)
    result = average_score
    return result

print(solution())