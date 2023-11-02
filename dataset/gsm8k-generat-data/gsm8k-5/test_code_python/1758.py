def solution():
    lizzie_score = 4
    nathalie_score = lizzie_score + 3
    combined_score = lizzie_score + nathalie_score
    aimee_score = 2 * combined_score
    total_score = lizzie_score + nathalie_score + aimee_score

    # Calculate the points made by their teammates
    teammate_score = 50 - total_score
    result = teammate_score
    return result

print(solution())