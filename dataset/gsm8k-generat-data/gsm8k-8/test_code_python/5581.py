def solution():
    # Define the number of students in the 6th grade
    students = 40

    # Calculate the number of students who wear glasses
    glasses = 0.25 * students

    # Calculate the number of students who wear contact lenses
    contacts = 0.4 * students

    # Calculate the number of students who do not wear any vision assistance
    none = students - glasses - contacts
    result = none
    return result

print(solution())