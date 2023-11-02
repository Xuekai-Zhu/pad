def solution():
    """After complaints from the residents of Tatoosh about the number of cats on the island, the wildlife service carried out a relocation mission that saw the number of cats on the island drastically reduced. On the first relocation mission, 600 cats were relocated from the island to a neighboring island. On the second mission, half of the remaining cats were relocated to a rescue center inland. If the number of cats originally on the island was 1800, how many cats remained on the island after the rescue mission?"""
    # Define the initial number of cats on the island
    initial_cats = 1800

    # Calculate the number of cats relocated on the first mission
    first_mission_cats = 600

    # Calculate the number of cats remaining after the first mission
    cats_remaining = initial_cats - first_mission_cats

    # Calculate the number of cats relocated on the second mission
    second_mission_cats = cats_remaining // 2

    # Calculate the final number of cats remaining on the island
    cats_remaining = cats_remaining - second_mission_cats

    # Display the final number of cats
    result = cats_remaining
    return result

print(solution())