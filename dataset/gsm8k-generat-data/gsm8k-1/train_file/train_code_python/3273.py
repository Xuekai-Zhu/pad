def solution():
    """There's a Bobbit worm hiding in the bottom of James' aquarium. Every day it eats 2 fish. After two weeks, James adds 8 more fish to the aquarium. A week later, he discovers the Bobbit worm. If the aquarium had 60 fish to start with, how many does it have when James discovers the Bobbit worm?"""
    initial_fish = 60
    days_before_discovery = 21
    fish_eaten = days_before_discovery * 2
    fish_after_two_weeks = initial_fish - fish_eaten
    fish_after_addition = fish_after_two_weeks + 8
    result = fish_after_addition
    return result

print(solution())