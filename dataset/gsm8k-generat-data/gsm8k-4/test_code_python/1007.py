def solution():
    """Rajesh walked 10 kilometers less than 4 times the distance that Hiro walked. Together they walked 25 kilometers. How many kilometers did Rajesh walk?"""
    # Define the distance Hiro walked
    hiro_distance = None

    # Define the distance Rajesh walked
    rajesh_distance = None

    total_distance = 25

    hiro_distance = total_distance / 5

    rajesh_distance = 4 * hiro_distance - 10

    result = rajesh_distance
    return result

print(solution())