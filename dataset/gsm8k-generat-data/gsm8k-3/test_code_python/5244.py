def solution():
    """Jackson collects 45 hermit crabs, 3 spiral shells per hermit crab, and 2 starfish per spiral shell. How many souvenirs does he collect total?"""
    # Define the number of hermit crabs and spiral shells per hermit crab
    HERMIT_CRAB_COUNT = 45
    SPIRAL_SHELLS_PER_CRAB = 3

    # Define the number of starfish per spiral shell
    STARFISH_PER_SHELL = 2

    # Calculate the total number of spiral shells
    total_spiral_shells = HERMIT_CRAB_COUNT * SPIRAL_SHELLS_PER_CRAB

    # Calculate the total number of starfish
    total_starfish = total_spiral_shells * STARFISH_PER_SHELL

    # Calculate the total number of souvenirs
    total_souvenirs = HERMIT_CRAB_COUNT + total_spiral_shells + total_starfish

    # Display the total number of souvenirs
    result = total_souvenirs
    return result

print(solution())