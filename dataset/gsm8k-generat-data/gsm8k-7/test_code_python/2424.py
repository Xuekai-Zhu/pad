def solution():
    bryan_score = 20
    jen_score = bryan_score + 10
    sammy_score = jen_score - 2
    total_points = 35

    # Calculate the total number of correct answers from Bryan and Jen
    bryan_and_jen_correct = bryan_score + jen_score

    # Calculate the number of mistakes made by Bryan and Jen
    bryan_and_jen_mistakes = total_points - bryan_and_jen_correct

    # Calculate the number of mistakes made by Sammy
    sammy_mistakes = bryan_and_jen_mistakes - (total_points - sammy_score)

    result = sammy_mistakes
    return result

print(solution())