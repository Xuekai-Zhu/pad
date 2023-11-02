def solution():
    attendees_A = 30
    attendees_B = 2 * attendees_A
    attendees_C = attendees_A + 10
    attendees_D = attendees_C - 5
    total_attendees = attendees_A + attendees_B + attendees_C + attendees_D

    not_from_ABCD = 185 - total_attendees
    result = not_from_ABCD
    return result

print(solution())