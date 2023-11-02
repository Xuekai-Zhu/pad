def solution():
    """Alex is getting ready to attend an event that she has hosted and wants to make sure that she has enough seats for everyone. She invites 100 people via email and each invited person says that they will also invite 2 of their friends. She then calls 10 of her friends to invite them too and 8 of them say they will be bringing their spouses. How many seats will Alex need?"""
    email_invites = 100
    friends_invites = 10
    guests_per_invite = 2
    spouses_per_guest = 1
    total_guests = (email_invites * guests_per_invite) + (friends_invites * guests_per_invite) + (friends_invites * spouses_per_guest * 8)
    seats_needed = total_guests
    result = seats_needed
    return result

print(solution())