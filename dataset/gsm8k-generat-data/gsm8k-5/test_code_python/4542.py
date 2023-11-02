def solution():
    tank1_fish = 20  # Tank 1 has 20 fish
    tank2_fish = tank1_fish * 2  # Tank 2 has twice as many fish as Tank 1
    tank3_fish = tank1_fish * 2  # Tank 3 has twice as many fish as Tank 1

    # Calculate the total number of fish in all 3 tanks
    total_fish = tank1_fish + tank2_fish + tank3_fish
    result = total_fish
    return result

print(solution())