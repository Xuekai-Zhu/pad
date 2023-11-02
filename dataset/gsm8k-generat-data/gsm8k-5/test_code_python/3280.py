def solution():
    initial_fish = 14  # Jonah started with 14 small fish
    added_fish = 2  # Jonah added 2 more fish
    eaten_fish = 6  # The 2 new fish ate 6 of Jonah's original fish
    returned_fish = 2  # Jonah returned the 2 new fish to the store
    exchanged_fish = 3  # Jonah exchanged the 2 new fish for 3 new ones

    # Calculate the total number of fish Jonah has now
    total_fish = initial_fish + added_fish - eaten_fish - returned_fish + exchanged_fish
    result = total_fish
    return result

print(solution())