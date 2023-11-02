def solution():
    # Determine if Tange Sazen is physically capable of performing secretary tasks
    can_type = True
    can_read_notes = True
    has_both_eyes_and_arms = False
    if can_type and can_read_notes and has_both_eyes_and_arms:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())