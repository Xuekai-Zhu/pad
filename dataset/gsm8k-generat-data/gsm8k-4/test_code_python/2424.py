def solution():
    """Bryan's score on a math exam is 20. Jen scored 10 more than Bryan while Sammy scored 2 fewer than Jen. If the math exam has 35 points in all, how many mistakes did Sammy make?"""
    # Define the total points and Bryan's score
    total_points = 35
    bryan_score = 20

    # Calculate Jen's score
    jen_score = bryan_score + 10

    # Calculate Sammy's score
    sammy_score = jen_score - 2

    # Calculate the total score of all three students
    total_score = bryan_score + jen_score + sammy_score

    # Calculate the number of mistakes made by Sammy
    mistakes = total_points - total_score

    # Return the result
    result = mistakes
    return result

print(solution())