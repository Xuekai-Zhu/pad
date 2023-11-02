def solution():
    # Calculate the expected number of guests and the percentage who won't show up
    expected_guests = 220
    no_show_percent = 5/100

    # Calculate the actual number of guests who will attend
    actual_guests = expected_guests * (1 - no_show_percent)
    result = actual_guests
    return result

print(solution())