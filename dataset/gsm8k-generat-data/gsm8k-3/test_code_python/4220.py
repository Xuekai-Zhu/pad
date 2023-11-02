def solution():
    """A warehouse store sells cartons of gum. Each carton contains 5 packs of gum, and there are 3 sticks of gum in each pack. Each brown box contains 4 cartons of gum. How many sticks of gum are there in 8 brown boxes?"""
    # Define the number of packs of gum per carton and the number of sticks of gum per pack
    PACKS_PER_CARTON = 5
    STICKS_PER_PACK = 3

    # Define the number of cartons per brown box
    CARTONS_PER_BOX = 4

    # Define the number of brown boxes
    BOXES = 8

    # Calculate the total number of packs of gum
    packs_of_gum = CARTONS_PER_BOX * PACKS_PER_CARTON * BOXES

    # Calculate the total number of sticks of gum
    sticks_of_gum = packs_of_gum * STICKS_PER_PACK

    # Display the total number of sticks of gum
    result = sticks_of_gum
    return result

print(solution())