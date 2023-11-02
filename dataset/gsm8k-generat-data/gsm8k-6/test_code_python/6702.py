def solution():
    # Calculate the number of attendees who were faculty or staff
    faculty_staff = 100 * 0.1  

    # Calculate the remaining number of attendees
    remaining_attendees = 100 - faculty_staff  

    # Calculate the number of girls who attended
    girls = (2/3) * remaining_attendees  

    # Calculate the number of boys who attended
    boys = remaining_attendees - girls  
    result = boys
    return result

print(solution())