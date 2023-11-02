def solution():
    """Sue works in a factory and every 30 minutes, a machine she oversees produces 30 cans of soda. How many cans of soda can one machine produce in 8 hours?"""
    # Define the number of cans produced in 30 minutes
    cans_per_half_hour = 30

    # Define the number of minutes in 8 hours
    minutes_in_8_hours = 8 * 60

    # Calculate the number of cans produced in 8 hours
    cans_in_8_hours = (minutes_in_8_hours / 30) * cans_per_half_hour

    # Return the result
    result = cans_in_8_hours
    return result

print(solution())