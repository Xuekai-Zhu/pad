def solution():
    lizzie_score = 4
    nathalie_score = lizzie_score + 3
    combined_score = lizzie_score + nathalie_score
    aimee_score = combined_score * 2
    total_score = lizzie_score + nathalie_score + aimee_score
    teammate_score = 50 - total_score
    result = teammate_score
    return result

print(solution())