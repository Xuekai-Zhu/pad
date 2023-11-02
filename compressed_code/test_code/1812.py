def solution():
    
    invitations = 200
    rsvp_percentage = 0.9
    show_up_percentage = 0.8
    no_gift_people = 10

    rsvp_count = invitations * rsvp_percentage
    show_up_count = rsvp_count * show_up_percentage
    gift_people_count = show_up_count - no_gift_people

    result = gift_people_count
    return result

print(solution())