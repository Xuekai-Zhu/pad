def solution():
    """Sean and Sierra invited 200 guests to their wedding. If 83% of the guests RSVP with a Yes response and 9% of the guests RSVP with a No response, how many guests did not respond at all?"""
    total_guests = 200
    yes_rsvp = total_guests * 0.83
    no_rsvp = total_guests * 0.09
    not_responded = total_guests - yes_rsvp - no_rsvp
    result = not_responded
    return result

print(solution())