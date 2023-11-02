def solution():
    """Rajesh walked 10 kilometers less than 4 times the distance that Hiro walked. Together they walked 25 kilometers. How many kilometers did Rajesh walk?"""
    total_distance = 25
    hiro_distance = (total_distance / 5) * 1
    rajesh_distance = (total_distance / 5) * 4 - 10
    result = rajesh_distance
    return result

print(solution())