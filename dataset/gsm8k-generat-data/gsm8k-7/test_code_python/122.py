def solution():
    num_chairs = 40
    capacity_per_chair = 2
    num_members = capacity_per_chair

    # Calculate the number of chairs that were not occupied
    num_unoccupied_chairs = (2/5) * num_chairs

    # Calculate the number of chairs that were occupied
    num_occupied_chairs = num_chairs - num_unoccupied_chairs

    # Calculate the total number of members who attended the meeting
    num_attendees = num_occupied_chairs / capacity_per_chair
    result = num_attendees
    return result

print(solution())