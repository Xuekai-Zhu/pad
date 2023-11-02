def solution():
    """Martin is organizing a party, and he invited many of his colleagues. He invited 5 people from his hometown and twice as many people from his school. Martin invited also as many people from his sports club as the sum of people invited from his hometown and his school. The remaining invitations represent 20% of the total previously mentioned. How many people can potentially come to the party Martin is organizing?"""
    hometown_people = 5
    school_people = 2 * hometown_people
    sports_club_people = hometown_people + school_people
    total_people = hometown_people + school_people + sports_club_people
    remaining_invitations = 0.2 * total_people
    potential_attendees = total_people + remaining_invitations
    result = potential_attendees
    return result

print(solution())