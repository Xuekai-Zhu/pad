def solution():
    """Olaf has an aquarium. He has fish in 3 different colors: orange, green, and blue. Blue fish make up half of all the fish in the aquarium. There are 15 fewer orange fish than blue fish. How many green fish are there when the total number of fish in the aquarium is 80?"""
    # Define the total number of fish in the aquarium
    total_fish = 80

    # Calculate the number of blue fish
    blue_fish = total_fish / 2

    # Calculate the number of orange fish
    orange_fish = blue_fish - 15

    # Calculate the number of green fish
    green_fish = total_fish - blue_fish - orange_fish

    # return the result
    result = green_fish
    return result

print(solution())