def solution():
    total_points = 35  # The math exam has a 35-point total
    bryan_score = 20  # Bryan's score is 20 points
    jen_score = bryan_score + 10  # Jen's score is 10 more than Bryan's
    sammy_score = jen_score - 2  # Sammy's score is 2 fewer than Jen's

    # Calculate the total number of mistakes they made
    total_mistakes = total_points - (bryan_score + jen_score + sammy_score)
    result = total_mistakes
    return result

print(solution())