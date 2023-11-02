def solution():
    """Eric sorted 150 colored pencils into 5 containers for his art class. Before class, another teacher brought him 30 more pencils. How many can he evenly distribute between the five containers now?"""
    # Define the number of colored pencils per container before the additional ones
    pencils_per_container = 150 / 5

    # Calculate the total number of colored pencils after the additional ones
    total_pencils = 150 + 30

    # Calculate the number of colored pencils Eric can evenly distribute per container
    even_distribution = total_pencils / 5

    # Display the number of colored pencils Eric can evenly distribute per container
    result = even_distribution - pencils_per_container
    return result

print(solution())