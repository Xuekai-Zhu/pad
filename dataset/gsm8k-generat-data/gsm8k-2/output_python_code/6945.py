def solution():
    """A ship left a port and headed due west, having 400 pounds of food for the journey's supply. After one day of sailing, 2/5 of the supplies had been used by the sailors in the ship. After another two days of sailing, the sailors used 3/5 of the remaining supplies. Calculate the number of supplies remaining in the ship to last the sailors until they dock."""
    starting_supplies = 400
    used_first_day = 2/5 * starting_supplies
    supplies_left_first_day = starting_supplies - used_first_day
    used_second_and_third_day = 3/5 * supplies_left_first_day * 2
    supplies_left = supplies_left_first_day - used_second_and_third_day
    result = supplies_left
    return result

print(solution())