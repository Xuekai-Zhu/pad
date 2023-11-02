def solution():
    """Gretchen, Mitzi, and Beth went bowling together. Gretchen bowled a 120. Mitzi bowled a 113. Beth bowled an 85. What was their average bowling score?"""
    # Get the scores of each person
    gretchen_score = 120
    mitzi_score = 113
    beth_score = 85

    # Calculate the sum of the scores
    total_score = gretchen_score + mitzi_score + beth_score

    # Calculate the average score
    average_score = total_score / 3

    # Display the average score
    result = average_score
    return result

print(solution())