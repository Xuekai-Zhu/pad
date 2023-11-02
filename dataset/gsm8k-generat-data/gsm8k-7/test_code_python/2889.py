def solution():
    total_guests = 200
    yes_rsvp_percent = 0.83
    no_rsvp_percent = 0.09

    # Calculate the number of guests who RSVP'd with a Yes
    yes_rsvp = total_guests * yes_rsvp_percent

    # Calculate the number of guests who RSVP'd with a No
    no_rsvp = total_guests * no_rsvp_percent

    # Calculate the number of guests who did not respond
    no_response = total_guests - yes_rsvp - no_rsvp
    result = no_response
    return result

print(solution())