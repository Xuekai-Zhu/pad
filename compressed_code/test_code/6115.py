def solution():
    
    hometown = 5
    school = 2 * hometown
    club = hometown + school
    total_invites = hometown + school + club
    remaining_invites = 0.2 * total_invites
    potential_attendees = total_invites + remaining_invites
    result = potential_attendees
    return result

print(solution())