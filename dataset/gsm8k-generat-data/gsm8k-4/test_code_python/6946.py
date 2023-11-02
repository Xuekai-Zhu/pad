def solution():
    """A ship left a port and headed due west, having 400 pounds of food for the journey's supply. After one day of sailing, 2/5 of the supplies had been used by the sailors in the ship. After another two days of sailing, the sailors used 3/5 of the remaining supplies. Calculate the number of supplies remaining in the ship to last the sailors until they dock."""
    # Define the initial supply of food
    supply = 400

    # Calculate the amount of food used after one day of sailing
    used_after_one_day = supply * (2/5)

    # Calculate the remaining supply after one day of sailing
    remaining_after_one_day = supply - used_after_one_day

    # Calculate the amount of food used after two more days of sailing
    used_after_two_more_days = remaining_after_one_day * (3/5)

    # Calculate the remaining supply after three days of sailing
    remaining_after_three_days = remaining_after_one_day - used_after_two_more_days

    result = remaining_after_three_days
    return result

print(solution())