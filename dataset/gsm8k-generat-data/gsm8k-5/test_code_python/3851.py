def solution():
    distance_spain_germany = 1615  # Distance between Spain and Germany
    distance_spain_russia = 7019  # Distance between Spain and Russia
    distance_germany_russia = distance_spain_russia - distance_spain_germany  # Distance between Germany and Russia
    total_distance = distance_spain_germany + distance_germany_russia + distance_spain_germany  # Total distance for the round-trip from Spain to Russia
    result = total_distance
    return result

print(solution())