def solution():
    # Calculate the area of the painting and the area of the wall
    area_painting = 2 * 4   # feet
    area_wall = 5 * 10     # feet

    # Calculate the percentage of the wall taken up by the painting
    percent_taken_up = (area_painting / area_wall) * 100
    result = percent_taken_up
    return result

print(solution())