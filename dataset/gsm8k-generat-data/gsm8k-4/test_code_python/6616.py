def solution():
    """In Grade 4, there are two sections -- Diligence and Industry. The two sections have an equal number of students after 2 students were transferred from section Industry to Diligence. How many students were there in section Diligence before the transfer if, in both sections combined, there are a total of 50 students?"""
    # Define the total number of students
    total_students = 50

    # Calculate the initial number of students in each section
    initial_students = total_students / 2

    # Calculate the number of students in section Diligence before the transfer
    diligence_students = initial_students + 1

    # return the result
    result = diligence_students
    return result

print(solution())