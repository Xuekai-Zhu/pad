def solution():
    
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