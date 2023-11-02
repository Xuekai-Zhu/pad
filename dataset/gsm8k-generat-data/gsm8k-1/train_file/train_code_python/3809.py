def solution():
    """Danielle's apartment has 6 rooms. Heidi's apartment has 3 times as many rooms as Danielle's apartment. Grant's apartment has 1/9 as many rooms as Heidi's apartment. How many rooms does Grant's apartment have?"""
    danielles_rooms = 6
    heidis_rooms = danielles_rooms * 3
    grants_rooms = heidis_rooms / 9
    result = grants_rooms
    return result

print(solution())