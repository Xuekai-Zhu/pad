def solution():
    total_questions = 35  # there are 35 questions in the contest
    riley_mistakes = 3  # Riley got 3 mistakes
    ofelia_score = (total_questions - riley_mistakes) / 2 + 5  # Ofelia got 5 more than half of Riley's score

    # Calculate the total mistakes of the team
    total_mistakes = riley_mistakes + (total_questions - riley_mistakes - ofelia_score)

    result = total_mistakes
    return result

print(solution())