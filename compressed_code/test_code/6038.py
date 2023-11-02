def solution():
    
    expected_attendees = 220
    percent_not_attending = 5
    actual_attendees = expected_attendees * (1 - percent_not_attending / 100)
    result = actual_attendees
    return result

print(solution())