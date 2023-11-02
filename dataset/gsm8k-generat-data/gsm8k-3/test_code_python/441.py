def solution():
    """Martin is organizing a party, and he invited many of his colleagues. He invited 5 people from his hometown and twice as many people from his school. Martin invited also as many people from his sports club as the sum of people invited from his hometown and his school. The remaining invitations represent 20% of the total previously mentioned. How many people can potentially come to the party Martin is organizing?"""
    # Calculate the number of people invited from Martin's hometown
    hometown_guests = 5

    # Calculate the number of people invited from Martin's school
    school_guests = 2 * hometown_guests

    # Calculate the number of people invited from Martin's sports club
    sports_guests = hometown_guests + school_guests

    # Calculate the total number of invitations
    total_invites = hometown_guests + school_guests + sports_guests

    # Calculate the number of remaining invitations
    remaining_invites = total_invites * 0.2

    # Calculate the potential number of guests at the party
    potential_guests = total_invites + remaining_invites

    # Display the potential number of guests
    result = potential_guests
    return result

print(solution())