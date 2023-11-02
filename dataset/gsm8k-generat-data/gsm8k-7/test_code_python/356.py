def solution():
    # Each round has 5 questions and each correct answer earns 2 points
    points_per_question = 2
    questions_per_round = 5
    points_per_round = points_per_question * questions_per_round

    # If all questions are answered correctly, there's an additional 4 point bonus
    bonus_points = 4

    # Calculate the total number of points James earned
    total_points = (points_per_round + bonus_points) * 4  # 4 rounds with all questions answered correctly
    total_points += (points_per_round + points_per_question)  # 1 round with one question missed

    result = total_points
    return result

print(solution())