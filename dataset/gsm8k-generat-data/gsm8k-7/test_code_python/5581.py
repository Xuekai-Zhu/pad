def solution():
    num_students = 40
    glasses_percent = 0.25
    contacts_percent = 0.4

    # Calculate the number of students who wear glasses
    num_glasses = num_students * glasses_percent

    # Calculate the number of students who wear contacts
    num_contacts = num_students * contacts_percent

    # Calculate the number of students who do not wear any vision assistance
    num_no_assistance = num_students - num_glasses - num_contacts
    result = num_no_assistance
    return result

print(solution())