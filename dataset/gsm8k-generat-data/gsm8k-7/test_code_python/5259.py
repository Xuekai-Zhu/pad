def solution():
    current_fish = 20
    num_less_fish_caught = 4

    # Calculate the original number of fish in the tank
    original_fish = current_fish - num_less_fish_caught

    # Calculate the number of fish added to the tank
    num_added_fish = current_fish - original_fish
    result = num_added_fish
    return result

print(solution())