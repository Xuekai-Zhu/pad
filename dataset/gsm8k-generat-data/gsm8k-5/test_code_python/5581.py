def solution():
    students = 40  # There are 40 students in the 6th grade
    glasses_percentage = 25
    contacts_percentage = 40

    # Calculate the number of students who wear glasses
    glasses_count = int((glasses_percentage / 100) * students)

    # Calculate the number of students who wear contacts
    contacts_count = int((contacts_percentage / 100) * students)

    # Calculate the number of students who do not wear any vision assistance
    no_assistance_count = students - glasses_count - contacts_count
    result = no_assistance_count
    return result

print(solution())