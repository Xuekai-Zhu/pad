def solution():
    
    attendees_A = 30
    attendees_B = attendees_A * 2
    attendees_C = attendees_A + 10
    attendees_D = attendees_C - 5
    total_registered = attendees_A + attendees_B + attendees_C + attendees_D
    not_from_ABCD = 185 - total_registered
    result = not_from_ABCD
    return result

print(solution())