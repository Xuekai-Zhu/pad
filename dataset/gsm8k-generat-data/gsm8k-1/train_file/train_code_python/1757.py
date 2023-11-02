def solution():
    """In a Volleyball competition, Lizzie was able to score 4 points. Nathalie's score is 3 more than Lizzie's score and Aimee's score is twice the score of Lizzie and Nathalie combined. 
    The rest of the points were made by their teammates. If the whole team was able to score 50 points, how many points did their teammates make?"""
    lizzie_score = 4
    nathalie_score = lizzie_score + 3
    combined_score = lizzie_score + nathalie_score
    aimee_score = 2 * combined_score
    total_score = lizzie_score + nathalie_score + aimee_score
    teammate_score = 50 - total_score
    result = teammate_score
    return result

print(solution())