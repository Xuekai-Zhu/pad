def solution():
    """Clyde's four children wanted to go see their favorite band perform. The tickets were expensive so Clyde made a deal with his kids. If the average of their scores on their next math test was higher than 89, then he would buy them tickets to the concert. June earned a 97 on her math test, Patty earned an 85, Josh earned a 100 on his test and Henry earned a 94. What was their average math test score?"""
    june_score = 97
    patty_score = 85
    josh_score = 100
    henry_score = 94
    total_score = june_score + patty_score + josh_score + henry_score
    num_of_scores = 4
    average_score = total_score / num_of_scores
    result = average_score
    return result

print(solution())