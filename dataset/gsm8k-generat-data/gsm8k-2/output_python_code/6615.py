def solution():
    """In Grade 4, there are two sections -- Diligence and Industry. The two sections have an equal number of students after 2 students were transferred from section Industry to Diligence. How many students were there in section Diligence before the transfer if, in both sections combined, there are a total of 50 students?"""
    total_students = 50
    equal_students = total_students / 2
    diligence_students = equal_students + 2
    result = diligence_students
    return result

print(solution())