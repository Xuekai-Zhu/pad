def solution():
    """Wendy works at a chocolate factory packing chocolates. She can package 2 dozen chocolates in 5 minutes. How many individual chocolates can she package in 4 hours?"""
    # Define the number of chocolates in a dozen
    CHOCOLATES_PER_DOZEN = 12

    # Define the number of minutes per hour and the number of hours
    MINUTES_PER_HOUR = 60
    HOURS = 4

    # Define the number of chocolates Wendy can package in 5 minutes
    chocolates_per_5_minutes = 2 * CHOCOLATES_PER_DOZEN

    # Calculate the number of chocolates Wendy can package in 4 hours
    chocolates_in_4_hours = (MINUTES_PER_HOUR * HOURS / 5) * chocolates_per_5_minutes

    # Display the result
    result = chocolates_in_4_hours
    return result

print(solution())