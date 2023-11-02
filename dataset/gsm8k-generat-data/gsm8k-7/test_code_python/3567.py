def solution():
    total_students = 400
    invited_percent = 0.7
    revoked_percent = 0.4

    # Calculate the number of invited students who showed up
    invited_students = total_students * invited_percent

    # Calculate the number of revoked invitations
    revoked_invites = invited_students * revoked_percent

    # Calculate the number of invited students who attended the party
    attended_students = invited_students - revoked_invites

    result = attended_students
    return result

print(solution())