def solution():
    """A warehouse store sells cartons of gum. Each carton contains 5 packs of gum, and there are 3 sticks of gum in each pack. Each brown box contains 4 cartons of gum. How many sticks of gum are there in 8 brown boxes?"""
    # Define the number of packs and sticks of gum in each carton
    PACKS_PER_CARTON = 5
    STICKS_PER_PACK = 3

    # Define the number of cartons in each brown box
    CARTONS_PER_BOX = 4

    # Calculate the total number of sticks of gum in each carton
    gum_per_carton = PACKS_PER_CARTON * STICKS_PER_PACK

    # Calculate the total number of sticks of gum in each brown box
    gum_per_box = gum_per_carton * CARTONS_PER_BOX

    # Calculate the total number of sticks of gum in 8 brown boxes
    gum_total = gum_per_box * 8

    # Return the result
    result = gum_total
    return result

print(solution())