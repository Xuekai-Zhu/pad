def solution():
    """There's a Bobbit worm hiding in the bottom of James' aquarium. Every day it eats 2 fish. After two weeks, James adds 8 more fish to the aquarium. A week later, he discovers the Bobbit worm. If the aquarium had 60 fish to start with, how many does it have when James discovers the Bobbit worm?"""
    starting_fish = 60
    bobbit_worm_days = 21
    bobbit_worm_fish_eaten = bobbit_worm_days * 2
    james_added_fish = 8
    total_fish = starting_fish + james_added_fish - bobbit_worm_fish_eaten
    result = total_fish
    return result

print(solution())