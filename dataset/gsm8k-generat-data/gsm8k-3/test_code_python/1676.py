def solution():
    """Mikaela was repainting her bathroom. She bought 16 containers of paint to cover the four equally-sized walls. At the last minute, she decided to put tile on one wall in the bathroom and paint flowers on the ceiling with one container of paint instead. How many containers of paint will she have left over?"""
    # Define the number of walls to be painted
    NUM_WALLS = 4

    # Define the number of paint containers required per wall
    CONTAINERS_PER_WALL = 4

    # Calculate the total number of paint containers required
    total_containers = NUM_WALLS * CONTAINERS_PER_WALL

    # Subtract one container for the ceiling flowers and one container for the tiled wall
    total_containers -= 2

    # Calculate the number of leftover containers
    leftover_containers = 16 - total_containers

    # Display the number of leftover containers
    result = leftover_containers
    return result

print(solution())