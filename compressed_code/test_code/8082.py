def solution():
    
    total_guests = 200
    yes_rsvp = total_guests * 0.83
    no_rsvp = total_guests * 0.09
    not_responded = total_guests - yes_rsvp - no_rsvp
    result = not_responded
    return result

print(solution())