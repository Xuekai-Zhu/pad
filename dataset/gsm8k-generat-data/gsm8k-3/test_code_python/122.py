def solution():
    """In a conference room, 40 chairs with a capacity of 2 people each were arranged in rows in preparation for the board meeting of a company, whose number of members was the same as the chairs' capacity. If 2/5 of the chairs were not occupied, and the rest each had two people, calculate the number of board members who did attend the meeting."""
    # Define the number of chairs and capacity
    num_chairs = 40
    capacity = 2

    # Calculate the total number of people who could attend the meeting
    total_capacity = num_chairs * capacity

    # Calculate the number of unoccupied chairs
    unoccupied_chairs = num_chairs * (2/5)

    # Calculate the number of people who attended the meeting
    num_attendees = (num_chairs - unoccupied_chairs) * capacity

    # return the result
    result = num_attendees
    return result

print(solution())