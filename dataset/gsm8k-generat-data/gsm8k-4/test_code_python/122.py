def solution():
    """In a conference room, 40 chairs with a capacity of 2 people each were arranged in rows in preparation for the board meeting of a company, whose number of members was the same as the chairs' capacity. If 2/5 of the chairs were not occupied, and the rest each had two people, calculate the number of board members who did attend the meeting."""
    # Define the number of chairs and their capacity
    chairs = 40
    capacity = 2

    # Calculate the number of chairs not occupied
    empty_chairs = chairs * (2/5)

    # Calculate the number of occupied chairs
    occupied_chairs = chairs - empty_chairs

    # Calculate the number of board members who attended the meeting
    board_members = occupied_chairs * capacity

    result = board_members
    return result

print(solution())