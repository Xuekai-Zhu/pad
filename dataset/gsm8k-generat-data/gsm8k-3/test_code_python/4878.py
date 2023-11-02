def solution():
    """Bugs are thriving in a garden of 30 plants. The bugs are very hungry today and completely ate 20 plants. The next day, they were still full and only ate half of the remaining plants. After that, they ate only 1 of the plants that were left. How many plants remain?"""
    # Define the initial number of plants and the number of plants the bugs ate
    total_plants = 30
    plants_eaten = 20

    # Calculate the number of plants remaining after the bugs ate 20
    plants_remaining = total_plants - plants_eaten

    # Calculate the number of plants the bugs ate the next day (half of remaining)
    plants_eaten = plants_remaining / 2

    # Calculate the number of plants remaining after the bugs ate half of the remaining
    plants_remaining = plants_remaining - plants_eaten

    # Calculate the number of plants the bugs ate the next day (1 plant)
    plants_eaten = 1

    # Calculate the final number of plants remaining
    plants_remaining = plants_remaining - plants_eaten

    # Display the final number of plants remaining
    result = plants_remaining
    return result

print(solution())