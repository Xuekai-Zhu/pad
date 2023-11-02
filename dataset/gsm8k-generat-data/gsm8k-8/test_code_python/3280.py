def solution():
    # Initialize variables
    original_fish = 14
    added_fish = 2
    eaten_fish = 6
    exchanged_fish = 3

    # Calculate the total number of fish after each step
    total_fish = original_fish + added_fish  # 16 fish
    total_fish -= eaten_fish  # 10 fish
    total_fish += exchanged_fish  # 13 fish

    result = total_fish
    return result

print(solution())