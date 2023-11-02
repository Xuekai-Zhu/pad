def solution():
    """In a math contest, Riley and Ofelia are on one team. The team's final score is obtained by adding the scores of the students of the same team. Out of the 35 questions, Riley got 3 mistakes while Ofelia got 5 more than half the score of Riley. How many incorrect answers did their team get?"""
    # Define the total number of questions
    total_questions = 35

    # Calculate the number of questions Riley answered correctly
    riley_correct = total_questions - 3

    # Calculate the score of Riley
    riley_score = riley_correct / total_questions

    # Calculate the score of Ofelia
    ofelia_score = (riley_score * 0.5) + 5

    # Calculate the number of questions Ofelia answered correctly
    ofelia_correct = ofelia_score * total_questions

    # Calculate the total number of incorrect answers
    total_incorrect = total_questions - riley_correct - ofelia_correct

    # Display the result
    result = total_incorrect
    return result

print(solution())