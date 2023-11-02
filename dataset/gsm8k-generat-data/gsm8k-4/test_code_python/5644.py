def solution():
    """Andrew has 2 3-hour appointments today. He spends the rest of his 8-hour workday stamping permit applications. If he can stamp 50 permit applications an hour, how many permits total does he stamp today?"""
    # Define the length of Andrew's appointments
    appointment_length = 3

    # Calculate the remaining hours Andrew has to work
    remaining_hours = 8 - (2 * appointment_length)

    # Calculate the number of permits Andrew can stamp during the remaining time
    permits_stamped = remaining_hours * 50

    # Return the result
    result = permits_stamped
    return result

print(solution())