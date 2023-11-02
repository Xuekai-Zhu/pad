def solution():
    """Mikaela was repainting her bathroom. She bought 16 containers of paint to cover the four equally-sized walls. At the last minute, she decided to put tile on one wall in the bathroom and paint flowers on the ceiling with one container of paint instead. How many containers of paint will she have left over?"""
    # Define the initial number of containers of paint
    initial_containers = 16

    # Subtract one for the wall with tiles and one for the ceiling with flowers
    final_containers = initial_containers - 2

    # Return the number of leftover containers of paint
    result = final_containers
    return result

print(solution())