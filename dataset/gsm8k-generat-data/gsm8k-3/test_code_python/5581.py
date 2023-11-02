def solution():
    """There are 40 students in the 6th  grade.  25% of them wear glasses and 40% of them wear contact lenses.  How many students do not wear any vision assistance wear?"""
    # Define the number of students and the percentages of those who wear glasses and contact lenses
    TOTAL_STUDENTS = 40
    GLASSES_PERCENTAGE = 0.25
    CONTACTS_PERCENTAGE = 0.4

    # Calculate the number of students who wear glasses and contacts
    glasses_students = int(TOTAL_STUDENTS * GLASSES_PERCENTAGE)
    contacts_students = int(TOTAL_STUDENTS * CONTACTS_PERCENTAGE)

    # Calculate the number of students who don't wear any vision assistance
    no_assistance_students = TOTAL_STUDENTS - glasses_students - contacts_students

    # Display the number of students who don't wear any vision assistance
    result = no_assistance_students
    return result

print(solution())