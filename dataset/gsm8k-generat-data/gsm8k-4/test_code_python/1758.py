def solution():
    """In a Volleyball competition, Lizzie was able to score 4 points. Nathalie's score is 3 more than Lizzie's score and Aimee's score is twice the score of Lizzie and Nathalie combined.
    The rest of the points were made by their teammates. If the whole team was able to score 50 points, how many points did their teammates make?"""
    
    # Calculate Nathalie's score
    nathalie_score = 4 + 3

    # Calculate the combined score of Lizzie and Nathalie
    combined_score = 4 + nathalie_score

    # Calculate Aimee's score
    aimee_score = combined_score * 2

    # Calculate the total score of Lizzie, Nathalie, and Aimee
    total_score = 4 + nathalie_score + aimee_score

    # Calculate the total score of their teammates
    teammates_score = 50 - total_score

    # Return the answer
    result = teammates_score
    return result

print(solution())