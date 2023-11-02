def solution():
    # Define the number of questions and Riley's mistakes
    num_questions = 35
    riley_mistakes = 3

    # Calculate Ofelia's score and mistakes
    ofelia_score = 0.5 * (num_questions - riley_mistakes) + 5
    ofelia_mistakes = num_questions - riley_mistakes - ofelia_score

    # Calculate the team's total mistakes
    total_mistakes = riley_mistakes + ofelia_mistakes
    result = total_mistakes
    return result

print(solution())