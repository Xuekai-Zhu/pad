def solution():
    # Calculate Jen's score
    bryan_score = 20
    jen_score = bryan_score + 10

    # Calculate Sammy's score
    sammy_score = jen_score - 2

    # Calculate the total points missed
    total_points_missed = 35 - (bryan_score + jen_score + sammy_score)

    # Calculate the number of mistakes Sammy made
    sammy_mistakes = total_points_missed / 2
    result = sammy_mistakes
    return result

print(solution())