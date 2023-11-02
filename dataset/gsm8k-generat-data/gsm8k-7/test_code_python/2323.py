def solution():
    num_invitations = 200
    percent_rsvp = 0.9
    percent_show_up = 0.8
    num_no_gift = 10

    # Calculate the number of people who RSVPed
    num_rsvp = num_invitations * percent_rsvp

    # Calculate the number of people who actually showed up
    num_show_up = num_rsvp * percent_show_up

    # Calculate the number of people who received a gift
    num_gift = num_show_up - num_no_gift

    # Calculate the number of thank you cards needed
    num_thank_you = num_gift
    result = num_thank_you
    return result

print(solution())