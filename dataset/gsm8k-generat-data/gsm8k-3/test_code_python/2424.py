def solution():
    """Bryan's score on a math exam is 20. Jen scored 10 more than Bryan while Sammy scored 2 fewer than Jen. If the math exam has 35 points in all, how many mistakes did Sammy make?"""
    # Define Bryan's score
    bryan_score = 20

    # Define Jen's score
    jen_score = bryan_score + 10

    # Define Sammy's score
    sammy_score = jen_score - 2

    # Calculate the total points earned by all three students
    total_score = bryan_score + jen_score + sammy_score

    # Calculate the number of mistakes made by Sammy
    mistakes = 35 - total_score

    # Display the number of mistakes made by Sammy
    result = mistakes
    return result

print(solution())