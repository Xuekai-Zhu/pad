def solution():
    starting_fish = 14
    added_fish = 2
    eaten_fish = 6
    exchanged_fish = 3

    # Calculate the total number of fish after adding the two additional fish
    total_fish = starting_fish + added_fish

    # Subtract the number of fish that were eaten
    total_fish -= eaten_fish

    # Add the number of fish exchanged for new ones
    total_fish += exchanged_fish

    result = total_fish
    return result

print(solution())