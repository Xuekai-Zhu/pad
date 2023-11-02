def solution():
    total_guests = 200
    yes_responses = 0.83 * total_guests
    no_responses = 0.09 * total_guests

    # Calculate the number of guests who did not respond
    no_response_guests = total_guests - yes_responses - no_responses
    result = no_response_guests
    return result

print(solution())