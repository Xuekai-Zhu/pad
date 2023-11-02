def solution():
    geography_score = 50
    math_score = 70
    english_score = 66

    # Calculate the average of the three scores and assign it as history score
    history_score = (geography_score + math_score + english_score) / 3

    # Calculate the total score across all four subjects
    total_score = geography_score + math_score + english_score + history_score
    result = total_score
    return result

print(solution())