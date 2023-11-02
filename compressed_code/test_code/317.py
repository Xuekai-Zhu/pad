def solution():
    
    hometown_people = 5
    school_people = 2 * hometown_people
    sports_club_people = hometown_people + school_people
    total_people = hometown_people + school_people + sports_club_people
    remaining_invitations = 0.2 * total_people
    potential_attendees = total_people + remaining_invitations
    result = potential_attendees
    return result

print(solution())