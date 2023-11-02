def solution():
    points_per_question = 2  # Students earn 2 points for each correct answer
    bonus_points = 4  # Students receive an additional 4 points for answering all questions correctly
    total_rounds = 5  # There are 5 rounds in the quiz bowl
    questions_per_round = 5  # Each round consists of 5 questions

    # Calculate total points earned by James in the quiz bowl
    total_correct_answers = (total_rounds * questions_per_round) - 1  # James missed one question
    total_points = (total_correct_answers * points_per_question) + bonus_points

    result = total_points
    return result

print(solution())