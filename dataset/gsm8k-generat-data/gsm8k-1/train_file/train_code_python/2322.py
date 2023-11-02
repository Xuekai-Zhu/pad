def solution():
    """Jack wants to send thank you cards to everyone who got him a gift for his wedding. He sent out 200 invitations. 90% of people RSVPed but only 80% of people who RSVPed actually showed up. Then 10 people who showed up didn't get a gift. How many thank you cards does he need?"""
    invitations_sent = 200
    rsvp_percent = 0.9
    show_up_percent = 0.8
    no_gift_people = 10
    
    rsvp_count = invitations_sent * rsvp_percent
    show_up_count = rsvp_count * show_up_percent
    gift_people_count = show_up_count - no_gift_people
    
    result = gift_people_count
    return result

print(solution())