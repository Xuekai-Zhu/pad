def solution():
    """In a math contest, Riley and Ofelia are on one team. The team's final score is obtained by adding the scores of the students of the same team. Out of the 35 questions, Riley got 3 mistakes while Ofelia got 5 more than half the score of Riley. How many incorrect answers did their team get?"""
    # Define the total number of questions
    total_questions = 35

    # Calculate Riley's score
    riley_score = total_questions - 3

    # Calculate Ofelia's score
    ofelia_score = (riley_score / 2) + 5

    # Calculate the team's total score
    team_score = riley_score + ofelia_score

    # Calculate the number of incorrect answers
    incorrect_answers = total_questions - team_score

    # Display the number of incorrect answers
    result = incorrect_answers
    return result

print(solution())