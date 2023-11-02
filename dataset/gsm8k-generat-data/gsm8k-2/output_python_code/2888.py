def solution():
    """Sean and Sierra invited 200 guests to their wedding. If 83% of the guests RSVP with a Yes response and 9% of the guests RSVP with a No response, how many guests did not respond at all?"""
    total_guests = 200
    yes_percent = 0.83
    no_percent = 0.09
    responded_percent = yes_percent + no_percent
    not_responded_percent = 1 - responded_percent
    not_responded_guests = not_responded_percent * total_guests
    result = not_responded_guests
    return result

print(solution())