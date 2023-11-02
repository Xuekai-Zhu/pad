def solution():
    """Laura is planning her wedding. She expects 220 people to attend the wedding, but she has been told that approximately 5% typically don't show. How many people will go to her wedding?"""
    expected_attendees = 220
    percent_not_attending = 5
    actual_attendees = expected_attendees * (1 - percent_not_attending / 100)
    result = actual_attendees
    return result

print(solution())