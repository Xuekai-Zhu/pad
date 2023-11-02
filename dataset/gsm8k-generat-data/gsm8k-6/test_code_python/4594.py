def solution():
    # Calculate the total number of attendees from companies A, B, C, and D
    total_attendees_ABCD = 30 + 2*30 + 10 + (10-5)  # 30 attendees from company A, company B has twice the attendees of A, company C has 10 more attendees than A, and company D has 5 fewer attendees than C
    # Calculate the number of attendees who are not from companies A, B, C or D
    non_ABCD_attendees = 185 - total_attendees_ABCD
    result = non_ABCD_attendees
    return result

print(solution())