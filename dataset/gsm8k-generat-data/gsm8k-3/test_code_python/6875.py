def solution():
    """A herring has 40 oz of fat, an eel 20 oz, and a pike 10 more oz of fat than an eel. If Ellianna cooked and served 40 fish of each type, calculate how many ounces of fat she served."""
    # Define the amount of fat in each type of fish
    HERRING_FAT = 40
    EEL_FAT = 20
    PIKE_FAT = EEL_FAT + 10

    # Define the number of each type of fish served
    NUM_FISH = 40

    # Calculate the total amount of fat served
    total_fat = (HERRING_FAT + EEL_FAT + PIKE_FAT) * NUM_FISH

    # Display the total amount of fat served
    result = total_fat
    return result

print(solution())