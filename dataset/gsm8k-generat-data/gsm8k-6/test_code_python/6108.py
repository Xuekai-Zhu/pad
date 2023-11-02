def solution():
    # Calculate the number of rooms in Heidi's apartment
    grant_rooms = 2  # number of rooms in Grant's apartment
    heidi_rooms = grant_rooms * 9  # Grant's apartment has 1/9 as many rooms as Heidi's apartment
    danielle_rooms = heidi_rooms / 3  # Heidi's apartment has 3 times as many rooms as Danielle's apartment
    result = danielle_rooms
    return result

print(solution())