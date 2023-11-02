def solution():
    """Out of the 80 students who took the biology exam, only 2/5 of them managed to score 100%. If a score below 80% qualified as failing, and 50 percent of the remaining students who didn't score 100% managed to score over 80%, calculate the number of students who failed the exam."""
    # Define the number of students who scored 100%
    score_100 = 2/5 * 80

    # Calculate the number of students who didn't score 100%
    not_100 = 80 - score_100

    # Calculate the number of students who scored over 80%
    over_80 = 0.5 * not_100

    # Calculate the number of students who failed
    failed = not_100 - over_80 + score_100

    # Display the number of students who failed
    result = failed
    return result

print(solution())