def solution():
    attendees_A = 30
    attendees_B = attendees_A * 2
    attendees_C = attendees_A + 10
    attendees_D = attendees_C - 5
    total_attendees = 185

    # Calculate the number of attendees from companies A, B, C and D
    attendees_ABCD = attendees_A + attendees_B + attendees_C + attendees_D

    # Calculate the number of attendees not from companies A, B, C or D
    other_attendees = total_attendees - attendees_ABCD
    result = other_attendees
    return result

print(solution())