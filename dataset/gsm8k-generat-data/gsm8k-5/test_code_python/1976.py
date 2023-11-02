def solution():
    total_boats = 30  # Madison makes 30 paper boats
    eaten_by_fish = total_boats * 0.2  # 20% of the boats are eaten by fish
    shot_with_arrows = 2  # Madison shoots two of the boats with flaming arrows

    # Calculate the number of boats left
    boats_left = total_boats - eaten_by_fish - shot_with_arrows
    result = boats_left
    return result

print(solution())