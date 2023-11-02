def solution():
    """3 cloves of garlic can repel 2 vampires, 8 vampire bats or 3 wights. How many cloves of garlic are needed to repel 30 vampires, 12 wights and 40 vampire bats?"""
    # Define the number of vampires, wights, and vampire bats that can be repelled by 3 cloves of garlic
    VAMPIRES_PER_GARLIC = 2/3
    WIGHTS_PER_GARLIC = 1
    VAMPIRE_BATS_PER_GARLIC = 8/3

    # Define the number of vampires, wights, and vampire bats that need to be repelled
    vampires_needed = 30
    wights_needed = 12
    vampire_bats_needed = 40

    # Calculate the number of cloves of garlic needed to repel each type of creature
    garlic_needed_for_vampires = vampires_needed / VAMPIRES_PER_GARLIC
    garlic_needed_for_wights = wights_needed / WIGHTS_PER_GARLIC
    garlic_needed_for_vampire_bats = vampire_bats_needed / VAMPIRE_BATS_PER_GARLIC

    # Calculate the total number of cloves of garlic needed to repel all the creatures
    total_garlic_needed = garlic_needed_for_vampires + garlic_needed_for_wights + garlic_needed_for_vampire_bats

    # Display the total number of cloves of garlic needed
    result = total_garlic_needed
    return result

print(solution())