def solution():
    """There's a Bobbit worm hiding in the bottom of James' aquarium. Every day it eats 2 fish. After two weeks, James adds 8 more fish to the aquarium. A week later, he discovers the Bobbit worm. If the aquarium had 60 fish to start with, how many does it have when James discovers the Bobbit worm?"""
    # Define the initial number of fish
    initial_fish = 60

    # Calculate the number of fish remaining after 2 weeks
    remaining_fish = initial_fish - (2 * 7 * 2)

    # Add the 8 new fish
    remaining_fish += 8

    # Calculate the number of fish remaining after one more week
    remaining_fish -= 7 * 2

    result = remaining_fish
    return result

print(solution())