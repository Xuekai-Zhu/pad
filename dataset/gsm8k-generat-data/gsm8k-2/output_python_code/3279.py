def solution():
    """Jonah decided to set up an aquarium. He started with 14 small fish. He added 2 more, but they ate 6 of his original fish before he could remove them and take them back to the store. He exchanged them for 3 new fish. How many fish does Jonah have now?"""
    starting_fish = 14
    added_fish = 2
    eaten_fish = 6
    exchanged_fish = 3
    total_fish = starting_fish + added_fish - eaten_fish + exchanged_fish
    result = total_fish
    return result

print(solution())