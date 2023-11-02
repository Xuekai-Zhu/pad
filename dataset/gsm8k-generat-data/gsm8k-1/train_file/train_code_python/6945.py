def solution():
    """A ship left a port and headed due west, having 400 pounds of food for the journey's supply. After one day of sailing, 2/5 of the supplies had been used by the sailors in the ship. After another two days of sailing, the sailors used 3/5 of the remaining supplies. Calculate the number of supplies remaining in the ship to last the sailors until they dock."""
    initial_supplies = 400
    first_day_used = initial_supplies * (2/5)
    remaining_supplies_after_first_day = initial_supplies - first_day_used
    next_two_days_used = remaining_supplies_after_first_day * (3/5)
    remaining_supplies = remaining_supplies_after_first_day - next_two_days_used
    result = remaining_supplies
    return result

print(solution())