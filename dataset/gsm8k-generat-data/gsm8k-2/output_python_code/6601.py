def solution():
    """In a math contest, Riley and Ofelia are on one team. The team's final score is obtained by adding the scores of the students of the same team. Out of the 35 questions, Riley got 3 mistakes while Ofelia got 5 more than half the score of Riley. How many incorrect answers did their team get?"""
    total_questions = 35
    riley_mistakes = 3
    riley_correct = total_questions - riley_mistakes
    ofelia_correct = (riley_correct * 0.5) + 5
    total_correct = riley_correct + ofelia_correct
    incorrect = total_questions - total_correct
    result = incorrect
    return result

print(solution())