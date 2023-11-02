def solution():
    
    expected_attendees = 220
    no_show_percent = 0.05
    actual_attendees = expected_attendees * (1 - no_show_percent)
    result = actual_attendees
    return result

print(solution())