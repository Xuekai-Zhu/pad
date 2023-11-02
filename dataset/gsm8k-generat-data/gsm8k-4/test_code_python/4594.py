def solution():
    """A company is hosting a seminar. So far, 30 attendees from company A have been registered; company B has twice the number of attendees of company A; company C has 10 more attendees than company A; company D has 5 fewer attendees than company C. If a total of 185 attendees have registered, how many attendees who registered are not from either company A, B, C or D?"""
    # Define the number of attendees from company A
    attendees_A = 30

    # Define the number of attendees from company B
    attendees_B = attendees_A * 2

    # Define the number of attendees from company C
    attendees_C = attendees_A + 10

    # Define the number of attendees from company D
    attendees_D = attendees_C - 5

    # Calculate the total number of attendees
    total_attendees = attendees_A + attendees_B + attendees_C + attendees_D

    # Calculate the number of attendees who are not from companies A, B, C, or D
    other_attendees = 185 - total_attendees

    result = other_attendees
    return result

print(solution())