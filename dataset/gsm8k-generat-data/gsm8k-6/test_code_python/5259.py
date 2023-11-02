def solution():
    # Let x be the number of fish in the tank before adding more fish
    # Then the number of fish caught is x - 4
    # After adding them to the tank, the total number of fish is 20
    # So we have x - 4 + added_fish = 20
    # Solving for added_fish, we get added_fish = 24 - x
    added_fish = 24 - 20  # since there are currently 20 fish in the tank
    result = added_fish
    return result

print(solution())