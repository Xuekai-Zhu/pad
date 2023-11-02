def solution():
    """Danielle's apartment has 6 rooms. Heidi's apartment has 3 times as many rooms as Danielle's apartment. Grant's apartment has 1/9 as many rooms as Heidi's apartment. How many rooms does Grant's apartment have?"""
    # Define the number of rooms in Danielle's apartment
    danielle_rooms = 6

    # Calculate the number of rooms in Heidi's apartment
    heidi_rooms = danielle_rooms * 3

    # Calculate the number of rooms in Grant's apartment
    grant_rooms = heidi_rooms / 9

    # Display the number of rooms in Grant's apartment
    result = grant_rooms
    return result

print(solution())