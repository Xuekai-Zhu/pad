def solution():
    # Calculate the number of blue fish in the aquarium
    blue_fish = 80 / 2  # Blue fish make up half of all the fish in the aquarium
    # Calculate the number of orange fish in the aquarium
    orange_fish = blue_fish - 15  # There are 15 fewer orange fish than blue fish
    # Calculate the number of green fish in the aquarium
    green_fish = 80 - blue_fish - orange_fish  # Total number of fish in the aquarium is 80
    result = green_fish
    return result

print(solution())