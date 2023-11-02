def solution():
    """Anna, Alison, and Jeff collect stamps. Anna had 37 stamps in her collection, Alison had 28 stamps in her collection, and Jeff had 31 stamps in his collection. Alison gave Anna half of her collection in exchange for a novel, and then Anna traded Jeff two bluebird stamps for one mountain stamp. How many stamps did Anna have in the end?"""
    # Define the number of stamps each person has
    ANNA_STAMPS = 37
    ALISON_STAMPS = 28
    JEFF_STAMPS = 31

    # Calculate how many stamps Alison gives Anna
    ALISON_TO_ANNA = ALISON_STAMPS // 2

    # Add the stamps Alison gives to Anna to Anna's collection
    ANNA_STAMPS += ALISON_TO_ANNA

    # Calculate how many stamps Anna trades with Jeff
    BLUEBIRD_TO_MOUNTAIN = 2 / 1

    # Subtract the stamps Anna trades with Jeff from Anna's collection
    ANNA_STAMPS -= BLUEBIRD_TO_MOUNTAIN

    # Display the total number of stamps Anna has in the end
    result = ANNA_STAMPS
    return result

print(solution())