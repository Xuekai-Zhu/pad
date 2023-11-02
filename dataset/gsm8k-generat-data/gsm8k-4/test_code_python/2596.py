def solution():
    """Henry scored 50 points on his Geography test, 70 on his Math test and 66 on his English test. If his History score is the average of these 3 scores, what was his total score across all 4 subjects?"""
    # Define the scores for each subject
    geography_score = 50
    math_score = 70
    english_score = 66

    # Calculate the history score as the average of the other scores
    history_score = (geography_score + math_score + english_score) / 3

    # Calculate the total score across all 4 subjects
    total_score = geography_score + math_score + english_score + history_score

    # Return the result
    result = total_score
    return result

print(solution())