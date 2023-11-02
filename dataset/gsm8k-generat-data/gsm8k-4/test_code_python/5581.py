def solution():
    """There are 40 students in the 6th  grade.  25% of them wear glasses and 40% of them wear contact lenses.  How many students do not wear any vision assistance wear?"""
    # Define the total number of grade 6 students
    total_students = 40

    # Calculate the number of students wearing glasses
    glasses_students = round(total_students * 0.25)

    # Calculate the number of students wearing contact lenses
    lenses_students = round(total_students * 0.4)

    # Calculate the number of students who wear both glasses and contact lenses
    both_students = round(total_students * 0.1)

    # Calculate the number of students who wear either glasses or contact lenses or both
    vision_students = glasses_students + lenses_students - both_students

    # Calculate the number of students who do not wear any vision assistance
    no_vision_students = total_students - vision_students

    return no_vision_students

print(solution())