def solution():
    # Calculate the number of chairs that were not occupied
    unoccupied_chairs = 2/5 * 40

    # Calculate the number of chairs that were occupied by 2 people each
    occupied_chairs = 40 - unoccupied_chairs
    attendees = occupied_chairs * 2  # each occupied chair had 2 people

    result = attendees
    return result

print(solution())