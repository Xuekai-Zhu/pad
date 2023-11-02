def solution():
    # Define the number of expected and potential guests
    expected_guests = 50
    potential_guests = 40

    # Calculate the total number of guests
    total_guests = expected_guests + potential_guests

    # Determine the number of gift bags needed
    gift_bags_needed = total_guests - 10 - 20

    # Return the number of additional gift bags needed
    result = gift_bags_needed
    return result

print(solution())