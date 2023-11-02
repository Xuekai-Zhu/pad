def solution():
    # Calculate the number of invited students who attended
    invited_attended = 0.7 * 400  # 70% of students who showed up were invited
    invited_revoked = 0.4 * invited_attended  # 40% of invited students had their invitation revoked
    invited_attended -= invited_revoked  # subtract revoked invitations from invited attendees
    result = invited_attended
    return result

print(solution())