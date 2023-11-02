def solution():
    """After complaints from the residents of Tatoosh about the number of cats on the island, the wildlife service carried out a relocation mission that saw the number of cats on the island drastically reduced. On the first relocation mission, 600 cats were relocated from the island to a neighboring island. On the second mission, half of the remaining cats were relocated to a rescue center inland. If the number of cats originally on the island was 1800, how many cats remained on the island after the rescue mission?"""
    # Define the initial number of cats
    initial_cats = 1800

    # Calculate the number of cats relocated on the first mission
    mission1_cats = 600

    # Calculate the number of cats remaining after the first mission
    remaining_cats = initial_cats - mission1_cats

    # Calculate the number of cats relocated on the second mission
    mission2_cats = remaining_cats / 2
    
    # Calculate the number of cats remaining after the second mission
    remaining_cats = remaining_cats - mission2_cats
    
    # return the result
    result = remaining_cats
    return result

print(solution())