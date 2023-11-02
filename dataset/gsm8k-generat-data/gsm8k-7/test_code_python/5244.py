def solution():
    num_hermit_crabs = 45
    num_spiral_shells_per_crab = 3
    num_starfish_per_shell = 2

    # Calculate the total number of spiral shells collected
    total_spiral_shells = num_hermit_crabs * num_spiral_shells_per_crab

    # Calculate the total number of starfish collected
    total_starfish = total_spiral_shells * num_starfish_per_shell

    # Calculate the total number of souvenirs collected
    total_souvenirs = num_hermit_crabs + total_spiral_shells + total_starfish
    result = total_souvenirs
    return result

print(solution())