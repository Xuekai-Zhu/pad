def solution():
    hermit_crabs = 45  # Jackson collects 45 hermit crabs
    spiral_shells = hermit_crabs * 3  # Jackson collects 3 spiral shells per hermit crab
    starfish = spiral_shells * 2  # Jackson collects 2 starfish per spiral shell

    # Calculate the total number of souvenirs Jackson collects
    total_souvenirs = hermit_crabs + spiral_shells + starfish
    result = total_souvenirs
    return result

print(solution())