def solution():
    """Jackson collects 45 hermit crabs, 3 spiral shells per hermit crab, and 2 starfish per spiral shell. How many souvenirs does he collect total?"""
    # Define the number of hermit crabs
    hermit_crabs = 45

    # Calculate the number of spiral shells
    spiral_shells = hermit_crabs * 3

    # Calculate the number of starfish
    starfish = spiral_shells * 2

    # Calculate the total number of souvenirs
    souvenirs = hermit_crabs + spiral_shells + starfish

    # return the result
    result = souvenirs
    return result

print(solution())