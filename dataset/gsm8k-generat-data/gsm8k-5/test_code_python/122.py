def solution():
    # Calculate the total number of chairs in the conference room
    total_chairs = 40

    # Calculate the number of chairs that were not occupied
    unoccupied_chairs = 2/5 * total_chairs

    # Calculate the number of chairs that were occupied
    occupied_chairs = total_chairs - unoccupied_chairs

    # Calculate the number of board members who attended the meeting
    board_members = occupied_chairs / 2
    result = board_members
    return result

print(solution())