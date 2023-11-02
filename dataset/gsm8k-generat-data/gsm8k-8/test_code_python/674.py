def solution():
    # Define variables for number of spots and open spots on each level
    spots_per_level = 100
    open_spots_level1 = 58
    open_spots_level2 = open_spots_level1 + 2
    open_spots_level3 = open_spots_level2 + 5
    open_spots_level4 = 31

    # Calculate the total number of open spots and full spots
    total_open_spots = open_spots_level1 + open_spots_level2 + open_spots_level3 + open_spots_level4
    total_full_spots = (4 * spots_per_level) - total_open_spots

    result = total_full_spots
    return result

print(solution())