def solution():
    # Calculate the total points made by Lizzie, Nathalie, and Aimee
    lizzie_score = 4
    nathalie_score = lizzie_score + 3
    combined_score = lizzie_score + nathalie_score
    aimee_score = 2 * combined_score

    # Calculate the total points made by the whole team
    total_score = lizzie_score + nathalie_score + aimee_score + teammates_score
    teammates_score = 50 - total_score

    result = teammates_score
    return result

print(solution())