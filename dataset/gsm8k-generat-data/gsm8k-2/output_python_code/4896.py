def solution():
    """Olaf has an aquarium. He has fish in 3 different colors: orange, green, and blue. Blue fish make up half of all the fish in the aquarium. There are 15 fewer orange fish than blue fish. How many green fish are there when the total number of fish in the aquarium is 80?"""
    total_fish = 80
    blue_fish = total_fish / 2
    orange_fish = blue_fish - 15
    green_fish = total_fish - blue_fish - orange_fish
    result = green_fish
    return result

print(solution())