def solution():
    hometown_invites = 5
    school_invites = 2 * hometown_invites
    club_invites = hometown_invites + school_invites

    total_invites = hometown_invites + school_invites + club_invites
    remaining_invites = total_invites * 0.2

    potential_attendees = total_invites + remaining_invites
    result = potential_attendees
    return result

print(solution())