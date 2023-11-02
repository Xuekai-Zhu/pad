def solution():
    """How many portions of 200 ml milk can Jasmine pour from a full 2-liter container of milk?"""
    # Define the volume of the milk container in milliliters
    milk_volume_ml = 2000

    # Define the volume of one portion in milliliters
    portion_volume_ml = 200

    # Calculate the number of portions that can be poured from the milk container
    portions = milk_volume_ml // portion_volume_ml

    result = portions
    return result

print(solution())