def solution():
    """Jack wants to send thank you cards to everyone who got him a gift for his wedding. He sent out 200 invitations. 90% of people RSVPed but only 80% of people who RSVPed actually showed up. Then 10 people who showed up didn't get a gift. How many thank you cards does he need?"""
    # Define the initial number of invitations and the percentages of RSVPs and show-ups
    invitations = 200
    rsvp_percent = 0.9
    show_up_percent = 0.8

    # Calculate the number of people who RSVPed and showed up
    rsvped = invitations * rsvp_percent
    showed_up = rsvped * show_up_percent

    # Calculate the number of people who showed up and got a gift
    got_gift = showed_up - 10

    # The number of thank you cards needed is the same as the number of people who got a gift
    result = got_gift
    return result

print(solution())