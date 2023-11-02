def solution():
    """Wendy works at a chocolate factory packing chocolates. She can package 2 dozen chocolates in 5 minutes. How many individual chocolates can she package in 4 hours?"""
    # Define the number of chocolates Wendy can package in 5 minutes
    chocolates_per_5_minutes = 2 * 12

    # Define the number of 5-minute intervals in 4 hours
    intervals_in_4_hours = 4 * 60 / 5

    # Calculate the total number of chocolates Wendy can package in 4 hours
    total_chocolates = chocolates_per_5_minutes * intervals_in_4_hours

    # return the result
    result = total_chocolates
    return result

print(solution())