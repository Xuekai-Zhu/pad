def solution():
    """Sean and Sierra invited 200 guests to their wedding.  If 83% of the guests RSVP with a Yes response and 9% of the guests RSVP with a No response, how many guests did not respond at all?"""
    # Define the total number of guests invited
    total_guests = 200

    # Calculate the number of guests who RSVPed with a Yes response
    yes_responses = total_guests * 0.83

    # Calculate the number of guests who RSVPed with a No response
    no_responses = total_guests * 0.09

    # Calculate the number of guests who did not respond
    no_response = total_guests - yes_responses - no_responses

    # Display the number of guests who did not respond
    result = no_response
    return result

print(solution())