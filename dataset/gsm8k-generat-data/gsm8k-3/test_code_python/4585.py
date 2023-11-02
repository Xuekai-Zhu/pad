def solution():
    """How many portions of 200 ml milk can Jasmine pour from a full 2-liter container of milk?"""
    # Define the volume of the full 2-liter container of milk
    FULL_VOLUME = 2000  # ml

    # Define the volume of each portion of milk
    PORTION_VOLUME = 200  # ml

    # Calculate the number of portions that can be poured from the full container
    num_portions = FULL_VOLUME // PORTION_VOLUME

    # Display the number of portions
    result = num_portions
    return result

print(solution())