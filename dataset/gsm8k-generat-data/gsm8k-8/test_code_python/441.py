def solution():
    # Calculate the number of colleagues invited
    hometown_invites = 5
    school_invites = 2 * hometown_invites
    sports_club_invites = hometown_invites + school_invites
    total_invites = hometown_invites + school_invites + sports_club_invites

    # Calculate the number of remaining invitations
    remaining_invites = 0.2 * total_invites

    # Calculate the total potential number of attendees
    potential_attendees = total_invites + remaining_invites
    result = potential_attendees
    return result

print(solution())