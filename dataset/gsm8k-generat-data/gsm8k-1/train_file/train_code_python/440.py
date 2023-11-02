def solution():
    """Martin is organizing a party, and he invited many of his colleagues. He invited 5 people from his hometown and twice as many people from his school. Martin invited also as many people from his sports club as the sum of people invited from his hometown and his school. The remaining invitations represent 20% of the total previously mentioned. How many people can potentially come to the party Martin is organizing?"""
    hometown = 5
    school = 2 * hometown
    club = hometown + school
    total_invites = hometown + school + club
    remaining_invites = 0.2 * total_invites
    potential_attendees = total_invites + remaining_invites
    result = potential_attendees
    return result

print(solution())