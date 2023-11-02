def solution():
    geography_score = 50
    math_score = 70
    english_score = 66

    # Calculate the total score across the three subjects
    total_subjects_score = geography_score + math_score + english_score

    # Calculate the average score of the three subjects
    history_score = total_subjects_score / 3

    # Calculate the total score across all four subjects
    total_score = total_subjects_score + history_score
    result = total_score
    return result

print(solution())