def solution():
    
    total_distance = 100
    initial_spots = 5
    moved_spots = 2
    moved_spot = 3
    remaining_spots = total_distance - initial_spots - moved_spots - moved_spot
    place_of_race = remaining_spots + 1
    result = place_of_race
    return result

print(solution())