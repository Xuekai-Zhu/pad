def solution():
    """Eric sorted 150 colored pencils into 5 containers for his art class. Before class, another teacher brought him 30 more pencils. How many can he evenly distribute between the five containers now?"""
    # Define the number of colored pencils sorted into each container before the additional pencils were given
    pencils_per_container = 150 / 5

    # Add the additional pencils to the total number of pencils
    total_pencils = 150 + 30

    # Calculate the number of colored pencils that can be evenly distributed to each container
    pencils_per_container_now = total_pencils / 5

    result = pencils_per_container_now - pencils_per_container
    return result

print(solution())