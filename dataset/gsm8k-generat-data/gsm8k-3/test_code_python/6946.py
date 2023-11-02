def solution():
    """A ship left a port and headed due west, having 400 pounds of food for the journey's supply. After one day of sailing, 2/5 of the supplies had been used by the sailors in the ship. After another two days of sailing, the sailors used 3/5 of the remaining supplies. Calculate the number of supplies remaining in the ship to last the sailors until they dock."""
    # Define the amount of supplies at the start of the journey
    supplies_start = 400

    # Calculate the amount of supplies used after one day of sailing
    supplies_used_day1 = 2/5 * supplies_start

    # Calculate the amount of supplies remaining after one day of sailing
    supplies_remaining_day1 = supplies_start - supplies_used_day1

    # Calculate the amount of supplies used after two more days of sailing
    supplies_used_day2_3 = 3/5 * supplies_remaining_day1 * 2

    # Calculate the amount of supplies remaining after three days of sailing
    supplies_remaining_day3 = supplies_remaining_day1 - supplies_used_day2_3

    # Display the amount of supplies remaining
    result = supplies_remaining_day3
    return result

print(solution())