def solution():
    """Each turtle lays a clutch of 20 eggs. If 40% of the eggs successfully hatch, how many hatchlings do 6 turtles produce?"""
    # Define the number of eggs per clutch
    EGGS_PER_CLUTCH = 20

    # Define the hatch rate
    HATCH_RATE = 0.4

    # Define the number of turtles
    NUM_TURTLES = 6

    # Calculate the total number of eggs laid
    total_eggs = EGGS_PER_CLUTCH * NUM_TURTLES

    # Calculate the number of hatchlings
    hatchlings = total_eggs * HATCH_RATE

    # Display the number of hatchlings
    result = hatchlings
    return result

print(solution())