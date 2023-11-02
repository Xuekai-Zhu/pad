def solution():
    num_goldfish = 8

    # Calculate the number of angelfish, which is 4 more than the number of goldfish
    num_angelfish = num_goldfish + 4

    # Calculate the number of guppies, which is twice the number of angelfish
    num_guppies = num_angelfish * 2

    # Calculate the total number of fish in the aquarium
    total_fish = num_goldfish + num_angelfish + num_guppies
    result = total_fish
    return result

print(solution())