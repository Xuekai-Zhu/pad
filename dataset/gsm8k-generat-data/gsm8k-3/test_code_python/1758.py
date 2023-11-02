def solution():
    """In a Volleyball competition, Lizzie was able to score 4 points. Nathalie's score is 3 more than Lizzie's score and Aimee's score is twice the score of Lizzie and Nathalie combined. The rest of the points were made by their teammates. If the whole team was able to score 50 points, how many points did their teammates make?"""
    # Define Lizzie's score
    lizzie_score = 4

    # Calculate Nathalie's score
    nathalie_score = lizzie_score + 3

    # Calculate the combined score of Lizzie and Nathalie
    combined_score = lizzie_score + nathalie_score

    # Calculate Aimee's score
    aimee_score = combined_score * 2

    # Calculate the total score of Lizzie, Nathalie, and Aimee
    total_score = lizzie_score + nathalie_score + aimee_score

    # Calculate the score made by their teammates
    teammates_score = 50 - total_score

    # Display the score made by their teammates
    result = teammates_score
    return result

print(solution())