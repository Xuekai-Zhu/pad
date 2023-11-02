def solution():
    geography_score = 50
    math_score = 70
    english_score = 66
    history_score = (geography_score + math_score + english_score) / 3  # History score is the average of these 3 scores

    # Calculate the total score across all 4 subjects
    total_score = geography_score + math_score + english_score + history_score
    result = total_score
    return result

print(solution())