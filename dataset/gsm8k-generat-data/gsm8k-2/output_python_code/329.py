def solution():
    """Laura is planning her wedding. She expects 220 people to attend the wedding, but she has been told that approximately 5% typically don't show. How many people will go to her wedding?"""
    expected_attendees = 220
    no_show_percent = 0.05
    actual_attendees = expected_attendees * (1 - no_show_percent)
    result = actual_attendees
    return result

print(solution())