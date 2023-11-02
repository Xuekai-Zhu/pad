def solution():
    water_per_kilometer = 60  # Hannah needs to drink 60 ml of water for each kilometer she runs
    laps_per_kilometer = 8  # Hannah needs to run 8 laps
    lap_distance = 0.25  # Each lap is 0.25 km

    # Calculate the total distance Hannah needs to run
    total_distance = laps_per_kilometer * lap_distance

    # Calculate the total amount of water Hannah needs to drink
    total_water = total_distance * water_per_kilometer
    result = total_water
    return result

print(solution())