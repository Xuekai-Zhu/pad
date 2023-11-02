def solution():
    # Calculate the number of people who RSVPed
    rsvp_count = 0.9 * 200

    # Calculate the number of people who actually showed up
    actual_count = 0.8 * rsvp_count

    # Calculate the number of people who received a gift
    gift_count = actual_count - 10

    # Calculate the number of thank you cards needed
    thank_you_count = gift_count

    return thank_you_count

print(solution())