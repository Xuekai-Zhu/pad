def solution():
    maths_marks = 70 * 0.9  # Amaya scored 1/10 less in Maths than in Music
    arts_marks = maths_marks + 20  # Amaya scored 20 marks fewer in Maths than in Arts
    ss_marks = 70 + 10  # Amaya got 10 marks more in Social Studies than in Music

    # Calculate the total marks scored in all subjects
    total_marks = maths_marks + arts_marks + ss_marks + 70  # 70 is the marks scored in Music
    result = total_marks
    return result

print(solution())