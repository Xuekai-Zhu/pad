def solution():
    """Rajesh walked 10 kilometers less than 4 times the distance that Hiro walked. Together they walked 25 kilometers. How many kilometers did Rajesh walk?"""
    # Let x be the distance that Hiro walked
    # Then Rajesh walked 4x - 10 kilometers
    # Together they walked x + (4x - 10) = 5x - 10 kilometers
    # And we know that 5x - 10 = 25
    # Solving for x:
    x = (25 + 10) / 5
    # Rajesh walked 4x - 10 kilometers
    rajesh_distance = 4*x - 10

    # Display Rajesh's distance
    result = rajesh_distance
    return result

print(solution())