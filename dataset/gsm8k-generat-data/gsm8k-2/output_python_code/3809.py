def solution():
    """Danielle's apartment has 6 rooms. Heidi's apartment has 3 times as many rooms as Danielle's apartment. Grant's apartment has 1/9 as many rooms as Heidi's apartment. How many rooms does Grant's apartment have?"""
    danielle_rooms = 6
    heidi_rooms = 3 * danielle_rooms
    grant_rooms = heidi_rooms / 9
    result = grant_rooms
    return result

print(solution())