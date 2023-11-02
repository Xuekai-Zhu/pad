def solution():
    # Calculate Amaya's score in Maths
    arts_score = 70 + 20
    maths_score = arts_score - 20
    maths_score = maths_score - (0.1 * maths_score)

    # Calculate Amaya's score in Social Studies
    ss_score = 70 + 10

    # Calculate the total marks
    total_marks = arts_score + maths_score + ss_score + 70
    result = total_marks
    return result

print(solution())