def solution():
    """In a guessing game, Hajar's score is 24 points. The difference in the scores between Hajar and Farah's score in the game is 21.
    What is the sum of their scores, assuming Farah's score is higher than Hajar's?"""
    # Define Hajar's score and the difference in scores
    hajar_score = 24
    score_diff = 21

    # Calculate Farah's score
    farah_score = hajar_score + score_diff

    # Calculate the sum of their scores
    total_score = hajar_score + farah_score

    # Display the total score
    result = total_score
    return result

print(solution())