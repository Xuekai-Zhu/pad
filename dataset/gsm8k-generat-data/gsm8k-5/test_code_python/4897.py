def solution():
    total_fish = 80  # Total number of fish in the aquarium
    blue_fish = total_fish / 2  # Blue fish make up half of all the fish
    orange_fish = blue_fish - 15  # There are 15 fewer orange fish than blue fish
    green_fish = total_fish - blue_fish - orange_fish  # Calculate the number of green fish

    result = green_fish
    return result

print(solution())