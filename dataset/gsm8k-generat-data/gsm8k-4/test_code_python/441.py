def solution():
    """Martin is organizing a party, and he invited many of his colleagues. He invited 5 people from his hometown and twice as many people from his school. Martin invited also as many people from his sports club as the sum of people invited from his hometown and his school. The remaining invitations represent 20% of the total previously mentioned. How many people can potentially come to the party Martin is organizing?"""
    # Calculate the number of people invited from Martin's hometown
    hometown_invites = 5

    # Calculate the number of people invited from Martin's school
    school_invites = hometown_invites * 2

    # Calculate the total number of people invited from Martin's sports club
    sports_club_invites = hometown_invites + school_invites

    # Calculate the total number of invitations sent
    total_invites = hometown_invites + school_invites + sports_club_invites

    # Calculate the number of invitations remaining
    remaining_invites = total_invites * 0.2

    # Calculate the total number of potential party attendees
    potential_attendees = total_invites + remaining_invites

    result = potential_attendees
    return result

print(solution())