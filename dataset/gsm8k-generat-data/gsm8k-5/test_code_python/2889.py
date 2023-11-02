def solution():
    total_guests = 200  # Sean and Sierra invited 200 guests
    yes_responses = 0.83 * total_guests  # 83% of the guests responded with a Yes
    no_responses = 0.09 * total_guests  # 9% of the guests responded with a No

    # Calculate the number of guests who did not respond
    no_response_guests = total_guests - yes_responses - no_responses
    result = no_response_guests
    return result

print(solution())