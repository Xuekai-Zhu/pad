def solution():
    """In a graduation ceremony, each graduate can bring their 2 parents. Twenty teachers and half as many administrators will also attend the graduation ceremony. If there are 50 graduates, how many chairs must be prepared for the ceremony?"""
    # Define the number of graduates and the number of accompanying persons
    graduates = 50
    accompanying_persons = graduates * 2

    # Calculate the number of teachers and administrators
    teachers = 20
    administrators = teachers / 2

    # Calculate the total number of people attending the ceremony
    total_attendees = graduates + accompanying_persons + teachers + administrators

    # Calculate the number of chairs needed
    chairs_needed = total_attendees

    # return the result
    result = chairs_needed
    return result

print(solution())