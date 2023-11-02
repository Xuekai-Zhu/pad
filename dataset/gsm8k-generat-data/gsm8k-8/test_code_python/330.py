def solution():
    # Define the expected number of guests and the percentage that typically don't show
    expected_guests = 220
    percentage_not_showing = 0.05

    # Calculate the number of people who are expected to attend the wedding
    actual_guests = expected_guests - (expected_guests * percentage_not_showing)
    result = actual_guests
    return result

print(solution())