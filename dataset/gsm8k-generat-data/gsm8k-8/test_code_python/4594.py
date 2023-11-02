def solution():
    # Define the number of attendees from each company
    a_attendees = 30
    b_attendees = 2 * a_attendees
    c_attendees = a_attendees + 10
    d_attendees = c_attendees - 5

    # Calculate the total number of attendees from the four companies
    total_attendees = a_attendees + b_attendees + c_attendees + d_attendees

    # Calculate the number of attendees not from the four companies
    other_attendees = 185 - total_attendees
    result = other_attendees
    return result

print(solution())