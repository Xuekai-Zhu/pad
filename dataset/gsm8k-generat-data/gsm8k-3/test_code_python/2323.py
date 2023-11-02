def solution():
    """Jack wants to send thank you cards to everyone who got him a gift for his wedding.  He sent out 200 invitations.  90% of people RSVPed but only 80% of people who RSVPed actually showed up.  Then 10 people who showed up didn't get a gift.  How many thank you cards does he need?"""
    # Get the number of people who RSVPed
    rsvp_count = 200 * 0.9

    # Get the number of people who actually showed up
    show_up_count = rsvp_count * 0.8

    # Subtract the number of people who didn't get a gift
    gift_count = show_up_count - 10

    # Jack needs to send a thank you card for each person who gave him a gift
    thank_you_count = gift_count

    # Display the number of thank you cards Jack needs to send
    result = thank_you_count
    return result

print(solution())