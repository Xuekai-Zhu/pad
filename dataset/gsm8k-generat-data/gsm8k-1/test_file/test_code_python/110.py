def solution():
    """Jamal's phone can hold 6 times more photographs than can Brittany's phone. The maximum number of photographs that Brittany's phone can hold is 50 times more than the number of birds in Jamal's photograph of the ducks at the zoo. If Jamal's phone can hold 1800 photographs, how many ducks can be seen in Jamal's photograph of ducks at the zoo?"""
    jamals_photos = 1800
    brittanys_photos = jamals_photos / 6
    ducks_in_birds = brittanys_photos / 50
    ducks_in_jamals_photo = ducks_in_birds
    result = ducks_in_jamals_photo
    return result

print(solution())