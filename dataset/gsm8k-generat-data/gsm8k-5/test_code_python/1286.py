def solution():
    yellow_fish = 12  # Olga has 12 yellow fish
    blue_fish = yellow_fish / 2  # Olga has half as many blue fish as yellow fish
    green_fish = yellow_fish * 2  # Olga has twice as many green fish as yellow fish

    # Calculate the total number of fish in Olga's aquarium
    total_fish = yellow_fish + blue_fish + green_fish
    result = total_fish
    return result

print(solution())