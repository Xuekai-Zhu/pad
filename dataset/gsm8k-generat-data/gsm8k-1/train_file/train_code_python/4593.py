def solution():
    """A company is hosting a seminar. So far, 30 attendees from company A have been registered; company B has twice the number of attendees of company A; company C has 10 more attendees than company A; company D has 5 fewer attendees than company C. If a total of 185 attendees have registered, how many attendees who registered are not from either company A, B, C or D?"""
    attendees_A = 30
    attendees_B = attendees_A * 2
    attendees_C = attendees_A + 10
    attendees_D = attendees_C - 5
    total_registered = attendees_A + attendees_B + attendees_C + attendees_D
    not_from_ABCD = 185 - total_registered
    result = not_from_ABCD
    return result

print(solution())