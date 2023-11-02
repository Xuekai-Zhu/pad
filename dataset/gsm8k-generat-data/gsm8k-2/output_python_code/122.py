def solution():
    """In a conference room, 40 chairs with a capacity of 2 people each were arranged in rows in preparation for the board meeting of a company, whose number of members was the same as the chairs' capacity. If 2/5 of the chairs were not occupied, and the rest each had two people, calculate the number of board members who did attend the meeting."""
    total_capacity = 40 * 2
    unoccupied_chairs = int(total_capacity * (2/5))
    occupied_chairs = total_capacity - unoccupied_chairs
    attended_members = int(occupied_chairs / 2)
    result = attended_members
    return result

print(solution())