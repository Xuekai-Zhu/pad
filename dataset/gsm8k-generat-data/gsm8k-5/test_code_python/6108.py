def solution():
    grant_rooms = 2  # Grant's apartment has 2 rooms
    heidi_rooms = 9 * grant_rooms  # Grant's apartment has 1/9 as many rooms as Heidi's apartment
    danielle_rooms = heidi_rooms / 3  # Heidi's apartment has 3 times as many rooms as Danielle's apartment

    result = danielle_rooms
    return result

print(solution())