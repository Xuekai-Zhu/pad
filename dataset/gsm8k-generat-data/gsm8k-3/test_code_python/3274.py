def solution():
    """There's a Bobbit worm hiding in the bottom of James' aquarium. Every day it eats 2 fish. After two weeks, James adds 8 more fish to the aquarium. A week later, he discovers the Bobbit worm. If the aquarium had 60 fish to start with, how many does it have when James discovers the Bobbit worm?"""
    # Define the number of fish in the aquarium at the start
    fish_count = 60

    # Calculate the number of fish James adds after two weeks
    added_fish = 8

    # Calculate the number of fish the Bobbit worm eats in two weeks
    eaten_fish = 2 * 14

    # Subtract the eaten fish and add the new fish to get the final count
    final_count = fish_count - eaten_fish + added_fish

    # Display the final count
    result = final_count
    return result

print(solution())