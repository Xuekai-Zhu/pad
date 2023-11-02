def solution():
    """Madison makes 30 paper boats and sets them afloat. 20% are eaten by fish and Madison shoots two of the others with flaming arrows. How many boats are left?"""
    initial_boats = 30
    eaten_by_fish = initial_boats * 0.2
    shot_by_flaming_arrows = 2
    boats_left = initial_boats - eaten_by_fish - shot_by_flaming_arrows
    result = boats_left
    return result

print(solution())