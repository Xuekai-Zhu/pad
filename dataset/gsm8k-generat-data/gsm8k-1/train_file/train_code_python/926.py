def solution():
    """Ashley had a birthday party and invited 20 of her friends, telling them to each invite one more person to attend the party. If half the number of the invited guests each came with one more person, what's the total number of people at the party, including Ashley?"""
    initial_invites = 20
    extra_invites = initial_invites * 1
    invited_guests = initial_invites + extra_invites
    extra_invites_2 = invited_guests / 2
    total_guests = initial_invites + extra_invites + extra_invites_2 + 1
    result = total_guests
    return result

print(solution())