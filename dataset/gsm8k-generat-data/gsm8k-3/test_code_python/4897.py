def solution():
    """Olaf has an aquarium. He has fish in 3 different colors: orange, green, and blue. Blue fish make up half of all the fish in the aquarium. There are 15 fewer orange fish than blue fish. How many green fish are there when the total number of fish in the aquarium is 80?"""
    # Define the proportion of blue fish
    BLUE_PROPORTION = 0.5

    # Calculate the number of blue fish
    total_fish = 80
    blue_fish = round(total_fish * BLUE_PROPORTION)

    # Calculate the number of orange fish
    orange_fish = blue_fish - 15

    # Calculate the number of green fish
    green_fish = total_fish - blue_fish - orange_fish

    # Display the number of green fish
    result = green_fish
    return result

print(solution())