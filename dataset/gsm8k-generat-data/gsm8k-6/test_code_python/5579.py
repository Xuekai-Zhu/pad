def solution():
    # Calculate the marks scored by Amaya in Maths, Arts and Social Studies
    maths_marks = 0.9 * (70 + 20)  # Amaya scored 1/10 less in Maths than Arts and scored 20 less in Maths than Arts
    arts_marks = 70 + 20  # Amaya scored 20 marks more in Arts than in Maths
    ss_marks = 70 + 10  # Amaya got 10 marks more in Social Studies than in Music

    # Calculate the total marks scored by Amaya in all subjects
    total_marks = maths_marks + arts_marks + ss_marks
    result = total_marks
    return result

print(solution())