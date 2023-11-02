def solution():
    """In a conference room, 40 chairs with a capacity of 2 people each were arranged in rows in preparation for the board meeting of a company, whose number of members was the same as the chairs' capacity. If 2/5 of the chairs were not occupied, and the rest each had two people, calculate the number of board members who did attend the meeting."""
    total_chairs = 40
    capacity_per_chair = 2
    occupied_chairs = total_chairs * (1 - 2/5)
    total_people = (occupied_chairs * 2) / capacity_per_chair
    result = total_people
    return result

print(solution())