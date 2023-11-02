def solution():
    """A company is hosting a seminar. So far, 30 attendees from company A have been registered; company B has twice the number of attendees of company A; company C has 10 more attendees than company A; company D has 5 fewer attendees than company C. If a total of 185 attendees have registered, how many attendees who registered are not from either company A, B, C or D?"""
    A = 30
    B = 2 * A
    C = A + 10
    D = C - 5
    total_registered = A + B + C + D
    not_ABCD = 185 - total_registered
    result = not_ABCD
    return result

print(solution())