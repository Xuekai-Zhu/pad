def solution():
    """Heidi's apartment has 3 times as many rooms as Danielle's apartment. Grant's apartment has 1/9 as many rooms as Heidi's apartment. If Grant's apartment has 2 rooms, how many rooms does Danielle's apartment have?"""
    # Define the number of rooms in Grant's apartment
    grant_rooms = 2

    # Calculate the number of rooms in Heidi's apartment
    heidi_rooms = grant_rooms * 9

    # Calculate the number of rooms in Danielle's apartment
    danielle_rooms = heidi_rooms / 3

    result = danielle_rooms
    return result

print(solution())