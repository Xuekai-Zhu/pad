def solution():
    total_score = 35  # total number of questions in the contest
    riley_mistakes = 3  # number of mistakes made by Riley
    riley_correct = total_score - riley_mistakes  # number of correct answers by Riley
    ofelia_correct = (riley_correct / 2) + 5  # half the score of Riley plus 5
    ofelia_mistakes = total_score - riley_mistakes - ofelia_correct  # number of mistakes made by Ofelia
    team_incorrect = riley_mistakes + ofelia_mistakes  # total number of incorrect answers by the team

    result = team_incorrect
    return result

print(solution())